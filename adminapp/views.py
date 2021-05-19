from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import AdminUserCreationForm, AdminUserEditForm, AdminProductEditForm
from mainapp.models import Product


# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан')
            return redirect('admin-staff:users')
    else:
        form = AdminUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def change_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = AdminUserEditForm(data=request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные сохранены')

            return redirect('admin-staff:users')
    else:
        form = AdminUserEditForm(instance=user)

    context = {
        'current_user': user,
        'form': form,
    }

    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()

    messages.success(request, f'Пользователь "{user.username}" удален')

    return redirect('admin-staff:users')


@user_passes_test(lambda u: u.is_superuser)
def activate_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()

    messages.success(request, f'Пользователь "{user.username}" активирован')

    return redirect('admin-staff:users')


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


def products(request):
    context = {
        'products': Product.objects.all()
    }

    return render(request, 'adminapp/admin-products-read.html', context)


def change_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AdminProductEditForm(data=request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные сохранены')

            return redirect('admin-staff:products')
    else:
        form = AdminProductEditForm(instance=product)

    context = {
        'current_product': product,
        'form': form,
    }

    return render(request, 'adminapp/admin-products-update-delete.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

    messages.success(request, f'Продукт "{product.name}" удален')

    return redirect('admin-staff:products')
