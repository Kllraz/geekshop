from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from django.utils.decorators import method_decorator
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


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = AdminUserCreationForm
    success_url = reverse_lazy('admin-staff:users')
    success_message = 'Пользователь создан'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = AdminUserEditForm
    success_url = reverse_lazy('admin-staff:users')
    success_message = 'Данные сохранены'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin-staff:users')
    success_message = 'Пользователь удален'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

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


class UsersListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UsersListView, self).dispatch(request, *args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = AdminCreateProductForm
    success_url = reverse_lazy('admin-staff:products')
    success_message = 'Продукт создан'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = AdminProductEditForm
    success_url = reverse_lazy("admin-staff:products")
    success_message = 'Данные сохранены'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/admin-product-category-update-delete.html'
    success_url = reverse_lazy('admin-staff:products')
    success_message = 'Продукт удален'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)

        return super(ProductDeleteView, self).delete(request, *args, **kwargs)


class ProductCategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-categories-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesListView, self).dispatch(request, *args, **kwargs)


class ProductCategoriesCreateView(SuccessMessageMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-create.html'
    form_class = AdminCreateProductCategoryForm
    success_url = reverse_lazy('admin-staff:product_categories')
    success_message = 'Категория создана'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesCreateView, self).dispatch(request, *args, **kwargs)


class ProductCategoriesUpdateView(SuccessMessageMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-update-delete.html'
    form_class = AdminEditProductCategoryForm
    success_url = reverse_lazy('admin-staff:product_categories')
    success_message = 'Данные сохранены'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesUpdateView, self).dispatch(request, *args, **kwargs)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-update-delete.html'
    success_url = reverse_lazy('admin-staff:product_categories')
    success_message = 'Категория удалена'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)

        return super(ProductCategoryDeleteView, self).delete(request, *args, **kwargs)
