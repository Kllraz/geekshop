from django.contrib import admin
from authapp.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('password', 'date_joined', 'last_login')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username', 'first_name', 'last_name')
