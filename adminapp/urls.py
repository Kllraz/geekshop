from django.urls import path

from adminapp.views import index, activate_user, UsersListView, ProductsListView, ProductCategoriesListView, \
    UserCreateView, \
    ProductCreateView, ProductCategoriesCreateView, UserUpdateView, ProductUpdateView, ProductCategoriesUpdateView, \
    UserDeleteView, ProductDeleteView, ProductCategoryDeleteView, OrderListView, OrderUpdateView, OrderDeleteView

app_name = 'authapp'

urlpatterns = [
    path('', index, name='index'),
    path('user-create/', UserCreateView.as_view(), name='create_user'),
    path('users/', UsersListView.as_view(), name='users'),
    path('user-change/<int:pk>/', UserUpdateView.as_view(), name='change_user'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    path('user-activate/<int:user_id>/', activate_user, name='activate_user'),

    path('products/', ProductsListView.as_view(), name='products'),
    path('product-create/', ProductCreateView.as_view(), name='create_product'),
    path('change-product/<int:pk>/', ProductUpdateView.as_view(), name='change_product'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('product-categories/', ProductCategoriesListView.as_view(), name='product_categories'),
    path('product-category-create/', ProductCategoriesCreateView.as_view(), name='create_product_category'),
    path('change-product-category/<int:pk>/', ProductCategoriesUpdateView.as_view(), name='change_product_category'),
    path('product-category-delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='delete_product_category'),

    path('orders/', OrderListView.as_view(), name='orders'),
    path('change-order/<int:pk>/', OrderUpdateView.as_view(), name='change_order'),
    path('cancel-order/<int:pk>/', OrderDeleteView.as_view(), name='cancel_order'),
]
