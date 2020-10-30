from django.db import models

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer

from prj.settings import BASE_URL

class Provider(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'


class Consumer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    address = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'


class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='category', null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="%s" />' % self.image.url)
        except:
            return 'None'


    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

class SubCategory(models.Model):
    name = models.CharField(max_length=250, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'SubCategories'
        ordering = ['category']


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = ImageCropField(upload_to='product', null=True, blank=True)
    cropping = ImageRatioField('image', '100x100')  # поле для хранения размера обрезки изображения
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL,  null=True, blank=True)

    @property
    def get_small_image(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_url)

    @property
    def get_small_image_url(self):
        try:
            return BASE_URL + get_thumbnailer(self.image).get_thumbnail({
                'size': (100, 100),
                'box': self.cropping,
                'crop': 'smart',
            }).url
        except:
            return BASE_URL+"Noimage.png"

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="%s" />' % self.image.url)
        except:
            return 'None'

    class Meta:
        ordering = ['category']


class Store(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):

    STATUS = (
        ('new', 'new oreder'),
        ('pending', 'pending order'),
        ('completed', 'completed order'),
    )

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, default='new', choices=STATUS)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ammount = models.IntegerField(default=0)
