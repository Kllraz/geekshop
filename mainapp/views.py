from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products_categories': ProductCategory.objects.all(),
    }
    # UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list:
    # <class 'mainapp.models.Product'> QuerySet.
    all_products = Product.objects.filter(category_id=category_id).order_by(
        'id') if category_id else Product.objects.all().order_by('id')
    paginator = Paginator(all_products, per_page=3)
    try:
        paginator_products = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        paginator_products = paginator.page(1)
    except EmptyPage:
        paginator_products = paginator.page(paginator.num_pages)

    context.update({'products': paginator_products})

    return render(request, 'mainapp/products.html', context)
