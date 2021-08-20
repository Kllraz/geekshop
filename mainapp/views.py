from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.list import ListView

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def product_categories():
    if settings.LOW_CACHE:
        key = 'product_categories'
        categories = cache.get(key)
        if categories is None:
            category = ProductCategory.objects.filter(is_delete=False)
            cache.set(key, category)
        return categories
    else:
        return ProductCategory.objects.filter(is_delete=False)


class ProductsListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    paginate_by = 3
    ordering = ('id',)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)

        context.update({
            'products_categories': ProductCategory.objects.all()
        })

        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        queryset = queryset.filter(
            category_id=self.kwargs.get('category_id'),
            is_deleted=False
        ) if self.kwargs.get('category_id') else queryset

        return queryset


def nav_ajax(request):
    if request.is_ajax():
        result = render_to_string(
            'mainapp/includes/nav-include.html',
            request=request)

        return JsonResponse({'result': result})


def basket_ajax(request):
    if request.is_ajax():
        total_cost = request.user.basket_set.first().total_sum

        return JsonResponse({'result': total_cost})