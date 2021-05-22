from django.urls import path

from adminapp.views import index, change_user, delete_user, activate_user, change_product, \
    delete_product, change_product_category, \
    delete_product_category

from adminapp.views import UsersListView, ProductsListView, ProductCategoriesListView, UserCreateView, \
    ProductCreateView, ProductCategoriesCreateView

app_name = 'authapp'

urlpatterns = [
    path('', index, name='index'),
    path('user-create/', UserCreateView.as_view(), name='create_user'),
    path('users/', UsersListView.as_view(), name='users'),
    path('user-change/<int:user_id>/', change_user, name='change_user'),
    path('user-delete/<int:user_id>/', delete_user, name='delete_user'),
    path('user-activate/<int:user_id>/', activate_user, name='activate_user'),

    path('products/', ProductsListView.as_view(), name='products'),
    path('product-create/', ProductCreateView.as_view(), name='create_product'),
    path('change-product/<int:product_id>/', change_product, name='change_product'),
    path('product-delete/<int:product_id>/', delete_product, name='delete_product'),

    path('product-categories/', ProductCategoriesListView.as_view(), name='product_categories'),
    path('product-category-create/', ProductCategoriesCreateView.as_view(), name='create_product_category'),
    path('change-product-category/<int:product_category_id>/', change_product_category, name='change_product_category'),
    path('product-category-delete/<int:product_category_id>/', delete_product_category, name='delete_product_category'),
]
