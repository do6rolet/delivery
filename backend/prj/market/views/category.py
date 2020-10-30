from django.shortcuts import render
from rest_framework import serializers  # описывают входные и выходные данные, их структуру, типы полей
from rest_framework import viewsets  # содержит generics
from rest_framework import permissions  # управляет правами доступа к endpoints

from market.models import Category, SubCategory


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify categories
    """

    queryset = Category.objects.all().order_by('-id')  # сюда заходят все записи, которые будут отдаваться на клиент
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # доступы для набора представлений
    http_method_names = ['get', 'post']  # список разрешенных запросов
