from django.conf import settings
from django.db import models

# Create your models here.
from mainapp.models import Product

#
# class OrderItemQuerySet(models.QuerySet):
#     def delete(self):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         super(OrderItemQuerySet, self).delete()


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    status = models.CharField(verbose_name='Статус',
                              max_length=3,
                              choices=ORDER_STATUS_CHOICES,
                              default=FORMING)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_quantity(self):
        items = self.orderitem.select_related()

        return sum((item.quantity for item in items))

    def get_product_type_quantity(self):
        items = self.orderitem.select_related()

        return len(items)

    def get_total_cost(self):
        items = self.orderitem.select_related()

        return sum((item.get_product_cost() for item in items))

    def get_summary(self):
        items = self.orderitem.select_related()
        return {
            'total_cost': sum((item.get_product_cost() for item in items)),
            'total_quantity': len(items)
        }
    # def delete(self, using=None, keep_parents=False):
    #     for item in self.orderitem.select_related():
    #         item.product.quantity += item.quantity
    #         item.product.save()
    #
    #     self.is_active = False
    #     self.save()


class OrderItem(models.Model):
    # objects = OrderItemQuerySet.as_manager()

    order = models.ForeignKey(Order, related_name='orderitem', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()

    # def delete(self, *args, **kwargs):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(OrderItem, self).delete(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - \
    #                                  self.OrderItem.get_item(self.pk).quantity
    #
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(OrderItem, self).save(*args, **kwargs)
