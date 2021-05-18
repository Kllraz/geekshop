from django.db import models
from authapp.models import User
from mainapp.models import Product


# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)

        return sum([basket.quantity for basket in baskets])

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)

        return sum([basket.sum() for basket in baskets])
