from django.core.management.base import BaseCommand, CommandError # будем наследоваться от этих классов

from market.models import Category, Product, SubCategory
from bs4 import BeautifulSoup # распознание html документов, и поиск нужных тегов
import requests # с помощью него будем совершать запросы по http к веб-сайту
from django.core.files import File # для загрузки картинки в БД
import shutil  # для работы с файловой системы
from prj.settings import BASE_DIR

from urllib3.exceptions import InsecureRequestWarning # используем для отключения вывода предупреждения
# о необходимости проверять сайт

STOP_WORDS = ['Авиа', 'авиа', 'дрон', 'Услуги', 'услуги', 'Послуги','послуги', 'авіації', 'вертольотами', 'вертолетом',
              'гвинтокрилом', 'кукурузником',    'Комплектация','ООО', 'Сельхозтехника',
              'ТОВ', 'ТД', 'ЧП', 'ТМ', 'Украин', 'Украина', 'Склад']

def get_products(cat, subcat, url):
    try:
        shutil.rmtree('%s/media/category/subcategory' % BASE_DIR)  # очищает католог от картинок
    except:
        pass
    print('Downloading fm %s' % url)
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    rez = requests.get(url, verify=False)
    soup = BeautifulSoup(rez.text, 'html.parser')
    for item in soup.findAll('div', {'class': 'company_pic'}):
        img = item.find('img')
        in_stop = False
        # отсеиваем ненужное
        for w in STOP_WORDS:
            if img.get('title').find(w) > -1:
                in_stop = True
        if img.get('src').find('no_image') > -1:
            in_stop = True

        if not in_stop:
            print(img.get('title'))
            pr = Product()
            pr.category = cat
            pr.name = img.get('title')
            pr.subcategory = subcat
            img_url = 'https://gastronoma.net/%s' % img.get('src')
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
            img_response = requests.get(img_url, stream=True, verify=False)
            # сохраняем временный файл
            with open('tmp.png', 'wb') as out_file:  # создается временный файл 'b' - binary, для записи 'w'-write
                shutil.copyfileobj(img_response.raw, out_file)
            # читаем временный файл и загружаем его программно в модель
            with open('%s/tmp.png' % BASE_DIR, 'rb') as img_file:
                pr.image.save('product.png', File(img_file), save=True)
            pr.save()






class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Clearing DB')
        # удаляем записи и картинки
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Product.objects.all().delete()
        try:
            shutil.rmtree('%s/media/category' % BASE_DIR) # очищает католог от картинок
        except:
            pass

        # достаем главную страницу и парсим
        URL = 'https://gastronoma.net'
        print('Start importing from %s' % URL)
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) # отключаем вывод предупреждения
        # о  необходимости проверять сайт (varify=False)
        rez = requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')

        # находим нужный div и в нем картинки
        content = soup.find('div', {'class': 'body_20'})
        for img in content.findAll('img'):
            c = Category()
            c.name = img.get('alt')
            img_url = 'https://gastronoma.net/%s' % img.get('src')
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
            img_response = requests.get(img_url, stream=True, verify=False)
            # сохраняем временный файл
            with open('tmp.png', 'wb') as out_file:  # создается временный файл 'b' - binary, для записи 'w'-write
                shutil.copyfileobj(img_response.raw, out_file)
            # читаем временный файл и загружаем его программно в модель
            with open('%s/tmp.png' % BASE_DIR, 'rb') as img_file:
                c.image.save('cat.png', File(img_file), save=True)
            c.save()
            # забираем подкатегории
            for subcat in img.find_parent('tr').find('div').findAll('a'):
                sc = SubCategory()
                sc.name = subcat.text
                sc.category = c
                sc.save()
                get_products(c, sc, subcat.get('href'))
            print('Saving... %s' % c.name)



