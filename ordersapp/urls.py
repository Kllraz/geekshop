from django.urls import path

from ordersapp.views import OrderListView, OrderCreateView, OrderUpdateView, OrderDelete, order_forming_complete, \
    OrderDetail, get_product_price

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('edit/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('detail/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('product/<int:pk>/price/', get_product_price, name='get_product_price')

]
