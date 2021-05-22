from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from authapp.models import User
from adminapp.forms import AdminUserCreationForm, AdminUserEditForm, AdminProductEditForm, AdminCreateProductForm, \
    AdminCreateProductCategoryForm, AdminEditProductCategoryForm
from mainapp.models import Product, ProductCategory


# Create your views here.

@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Менеджер').exists())
def index(request):
    return render(request, 'adminapp/admin.html')


# @user_passes_test(lambda u: u.is_superuser)

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = AdminUserCreationForm
    success_url = reverse_lazy('admin-staff:users')
    success_message = 'Пользователь создан'


# @user_passes_test(lambda u: u.is_superuser)
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = AdminUserEditForm
    success_url = reverse_lazy('admin-staff:users')
    success_message = 'Данные сохранены'


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


# @user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Менеджер').exists())
class UsersListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'


# @user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Менеджер').exists())
class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'


# @user_passes_test(lambda u: u.is_superuser)
class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = AdminCreateProductForm
    success_url = reverse_lazy('admin-staff:products')
    success_message = 'Продукт создан'


# @user_passes_test(lambda u: u.is_superuser)

class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = AdminProductEditForm
    success_url = reverse_lazy("admin-staff:products")
    success_message = 'Данные сохранены'


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

    messages.success(request, f'Продукт "{product.name}" удален')

    return redirect('admin-staff:products')


# @user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Менеджер').exists())
class ProductCategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-categories-read.html'


# @user_passes_test(lambda u: u.is_superuser)
class ProductCategoriesCreateView(SuccessMessageMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-create.html'
    form_class = AdminCreateProductCategoryForm
    success_url = reverse_lazy('admin-staff:product_categories')
    success_message = 'Категория создана'


class ProductCategoriesUpdateView(SuccessMessageMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-update-delete.html'
    form_class = AdminEditProductCategoryForm
    success_url = reverse_lazy('admin-staff:product_categories')
    success_message = 'Данные сохранены'


@user_passes_test(lambda u: u.is_superuser)
def delete_product_category(request, product_category_id):
    product_category = ProductCategory.objects.get(id=product_category_id)
    product_category.delete()

    messages.success(request, f'Категория "{product_category.name}" удалена')

    return redirect('admin-staff:product_categories')
