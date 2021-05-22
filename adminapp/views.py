from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin-staff:users')
    success_message = 'Пользователь удален'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        messages.success(request, self.success_message)

        return HttpResponseRedirect(success_url)


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


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/admin-product-category-update-delete.html'
    success_url = reverse_lazy('admin-staff:products')
    success_message = 'Продукт удален'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)

        return super(ProductDeleteView, self).delete(request, *args, **kwargs)


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


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-update-delete.html'
    success_url = reverse_lazy('admin-staff:product_categories')
    success_message = 'Категория удалена'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)

        return super(ProductCategoryDeleteView, self).delete(request, *args, **kwargs)
