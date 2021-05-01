from django.shortcuts import render
from authapp.forms import LoginForm, RegisterForm


# Create your views here.

def login(request):
    form = LoginForm()

    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    form = RegisterForm()

    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)
