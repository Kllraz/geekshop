from basketapp.models import Basket
from mainapp.models import Product
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

@login_required
def add_product(request, product_id=None):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_product(request, basket_id=None):
    if request.method == 'POST':
        Basket.objects.get(id=basket_id).delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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