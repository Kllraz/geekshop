from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from basketapp.models import Basket
from mainapp.models import Product
from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItem


class OrderListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = []
    context_object_name = 'object'
    success_url = reverse_lazy('ordersapp:order_list')

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = order_form_set(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)

            if len(basket_items):
                order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(basket_items))
                formset = order_form_set()

                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                    form.initial['price'] = basket_items[num].product.price
            else:
                formset = order_form_set()

        context.update({
            'orderitems': formset,
            'title': 'GeekShop - Создание заказа',
        })

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context.get('orderitems')

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()

            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            basket_items = Basket.objects.filter(
                user=self.request.user)  # при обновлении страницы создания заказа корзина очищалась, поэтому перенес
            basket_items.delete()

        if self.object.get_total_quantity() == 0:
            self.object.delete()

        return super(OrderCreateView, self).form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = []
    context_object_name = 'object'
    success_url = reverse_lazy('ordersapp:order_list')

    def get_context_data(self, **kwargs):
        context = super(OrderUpdateView, self).get_context_data(**kwargs)
        order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = order_form_set(self.request.POST, instance=self.object)
        else:
            queryset = self.object.orderitems.select_related()
            formset = order_form_set(instance=self.object, queryset=queryset)
            for form in formset.forms:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price

        context.update({
            'title': 'GeekShop - Редактирование заказа',
            'orderitems': formset,
        })

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems_form = context.get('orderitems')

        with transaction.atomic():
            self.object = form.save()

            if orderitems_form.is_valid():
                orderitems_form.instance = self.object
                orderitems_form.save()

        if self.object.get_total_quantity() == 0:
            self.object.delete()

        return super(OrderUpdateView, self).form_valid(form)


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:order_list')


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()

    return redirect('ordersapp:order_list')


class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context.update({
            'title': 'GeekShop - Просмотр заказа'
        })
        return context


def get_product_price(request, pk=None):
    if request.is_ajax():
        product = Product.objects.filter(id=pk).first()

        if product:
            product_price = product.price

            return JsonResponse({'price': product_price})
        else:
            return JsonResponse({'price': 0})


@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, update_fields, instance, **kwargs):
    if update_fields is 'quantity' or 'product':
        if instance.pk:
            instance.product.quantity -= instance.quantity - \
                                         sender.get_item(instance.pk).quantity
        else:
            instance.product.quantity -= instance.quantity
        instance.product.save()


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
