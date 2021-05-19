from django.contrib import admin
from mainapp.models import ProductCategory, Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    search_fields = ('name', 'category__name')
    ordering = ('quantity', 'price')
    fields = ('name', 'description', 'category', 'image', ('price', 'quantity'))


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
