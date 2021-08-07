from django.contrib import admin
from basketapp.models import Basket


# Register your models here.
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    ordering = ('user__username', 'quantity')
    search_fields = ('user__username', 'product__name')
