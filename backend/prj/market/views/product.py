from rest_framework.generics import ListAPIView
# from rest_framework.mixins import ListModelMixin
from market.models import Product
from market.views.category import CategorySerializer, SubCategorySerializer
from market.filters import ProductFilter
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'get_small_image_url']

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
