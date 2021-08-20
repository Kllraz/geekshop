from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

    @staticmethod
    def get_items():
        return ProductCategory.objects.filter(is_delete=False).order_by('name', 'discount')

    class Meta:
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} | {self.category.name}'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_deleted=False).order_by('category', 'name')