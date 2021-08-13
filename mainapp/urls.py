from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.views import ProductsListView, nav_ajax, basket_ajax

app_name = 'mainapp'

urlpatterns = [
    path('', cache_page(3600)(ProductsListView.as_view()), name='index'),
    path('<int:category_id>/', cache_page(3600)(ProductsListView.as_view()), name='product'),
    path('update-nav/', nav_ajax, name='nav_ajax'),
    path('update-basket/', basket_ajax, name='basket_ajax'),
]
