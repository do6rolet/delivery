from django_filters import rest_framework as filters
from market.models import Product


class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter()
    subcategory = filters.NumberFilter()
    searchkey = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'searchkey']
