from django.contrib import admin
from .models import *

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass # or you can use list_display = ['field_name1', 'field_name2',]

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    pass

# class ConsumerAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Consumer, ConsumerAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'get_small_image']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass

