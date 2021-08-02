from django.contrib import admin

# Register your models here.
from ordersapp.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name')
