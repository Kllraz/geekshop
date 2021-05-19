from django.urls import path

from adminapp.views import index, create_user, change_user, users, delete_user, activate_user, products, change_product, \
    delete_product, create_product, product_categories

app_name = 'authapp'

urlpatterns = [
    path('', index, name='index'),
    path('user-create/', create_user, name='create_user'),
    path('users/', users, name='users'),
    path('user-change/<int:user_id>/', change_user, name='change_user'),
    path('user-delete/<int:user_id>/', delete_user, name='delete_user'),
    path('user-activate/<int:user_id>/', activate_user, name='activate_user'),

    path('products/', products, name='products'),
    path('product-create/', create_product, name='create_product'),
    path('change-product/<int:product_id>/', change_product, name='change_product'),
    path('product-delete/<int:product_id>/', delete_product, name='delete_product'),

    path('product-categories/', product_categories, name='product_categories'),
    # path('change-product/<int:product_id>/', change_product, name='change_product'),
    # path('product-delete/<int:product_id>/', delete_product, name='delete_product'),
]
