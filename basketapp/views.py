from django.shortcuts import redirect

from basketapp.models import Basket
from mainapp.models import Product
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

@login_required
def add_product(request, product_id=None):
    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

        return JsonResponse({'status': True})
    return redirect('index')


@login_required
def remove_product(request, basket_id=None):
    if request.is_ajax():
        Basket.objects.get(id=basket_id).delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('basketapp/basket.html', context)

        return JsonResponse({'result': result})
    return redirect('index')


@login_required
def edit(request, basket_id=None, quantity=None):
    if request.is_ajax():
        basket = Basket.objects.get(id=basket_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('basketapp/basket.html', context)

        return JsonResponse({'result': result})

    return redirect('index')
