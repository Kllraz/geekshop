from django.urls import path

from basketapp.views import add_product, remove_product, edit

app_name = 'authapp'

urlpatterns = [
    path('add-product/<int:product_id>/', add_product, name='add_product'),
    path('remove-product/<int:basket_id>/', remove_product, name='remove_product'),
    path('edit/<int:basket_id>/<int:quantity>/', edit, name='edit')
]
