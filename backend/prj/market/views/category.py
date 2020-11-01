from django.shortcuts import render
from rest_framework import serializers  # описывают входные и выходные данные, их структуру, типы полей
from rest_framework import viewsets  # содержит generics
from rest_framework import permissions  # управляет правами доступа к endpoints
from rest_framework.generics import ListAPIView
from market.models import Category, SubCategory
from market.serializers.category import CategorySerializer
from market.serializers.subcategory import SubCategorySerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = None  # отключаем пагинатор

    def get_queryset(self):
        return Category.objects.all().order_by('-id')


class CategoryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify categories
    """

    queryset = Category.objects.all().order_by('-id')  # сюда заходят все записи, которые будут отдаваться на клиент
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # доступы для набора представлений
    http_method_names = ['get', 'post']  # список разрешенных запросов
