from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from authapp.forms import LoginForm, RegisterForm, EditForm
from authapp.models import User
from basketapp.models import Basket


# Create your views here.

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'authapp/login.html'

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context.update({
            'title': 'GeekShop - Авторизация'
        })

        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')
    form_class = RegisterForm
    success_message = 'Вы успешно зарегистрировались'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'GeekShop - Регистрация'
        })

        return context


class UserLogout(LogoutView):
    template_name = 'authapp/profile.html'
    next_page = reverse_lazy('index')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'authapp/profile.html'
    form_class = EditForm
    success_url = reverse_lazy('auth:profile')
    success_message = 'Данные сохранены'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'GeekShop - Профиль',
            'baskets': Basket.objects.filter(user=self.get_object())
        })

        return context
