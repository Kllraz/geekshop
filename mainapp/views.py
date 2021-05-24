from django.shortcuts import render
from django.views.generic.list import ListView

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


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
            category_id=self.kwargs.get('category_id')
        ) if self.kwargs.get('category_id') else queryset

        return queryset
