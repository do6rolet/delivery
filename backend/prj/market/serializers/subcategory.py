from rest_framework import serializers  # описывают входные и выходные данные, их структуру, типы полей
from market.models import SubCategory

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']