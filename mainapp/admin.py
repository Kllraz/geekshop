from django.contrib import admin
from mainapp.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    search_fields = ('name', 'category__name')
    ordering = ('quantity', 'price')
    fields = ('name', 'description', 'category', 'image', ('price', 'quantity'))
