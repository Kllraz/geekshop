from django.shortcuts import render, redirect
from authapp.forms import LoginForm, RegisterForm, EditForm
from django.contrib import auth, messages
from basketapp.models import Basket


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('auth:login')
    else:
        form = RegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)

    return redirect('index')


def profile(request):
    if request.method == 'POST':
        form = EditForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные сохранены')
    else:
        form = EditForm(instance=request.user)

    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user)
    }

    return render(request, 'authapp/profile.html', context)
