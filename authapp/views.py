from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from authapp.forms import LoginForm, RegisterForm, EditForm
from authapp.models import User

from django.core.mail import send_mail
from django.contrib import auth
from django.conf import settings
from django.shortcuts import redirect

from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


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


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = 'Активация аккаунта'
    message = f'Для активации аккаунта {user.email} на портале GeekShop перейдите по ссылке\n' \
              f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')
    form_class = RegisterForm
    success_message = 'Вы успешно зарегистрировались.\n' \
                      'Для активации аккаунта перейдите по ссылке из письма.'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'GeekShop - Регистрация'
        })

        return context

    def form_valid(self, form):
        form = super(UserCreateView, self).form_valid(form)
        send_verify_mail(self.object)

        return form


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.activation_key_expired() and not user.is_active:
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            logger.info(f'Аккаунт {user.email} активирован')

        return redirect('index')
    except User.DoesNotExist as error:
        messages.add_message(request, messages.ERROR, 'Ошибка активации аккаунта')
        logger.error(f'Ошибка активации: {error.args}')
        return redirect('auth:login')


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
        })

        return context
