from django.shortcuts import render
import json


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('mainapp/fixtures/products.json', 'r', encoding='utf-8') as file:
        decode_products = json.load(file, )

    context = {
        'title': 'GeekShop - Каталог',
        'products': decode_products
    }
    return render(request, 'mainapp/products.html', context)
