from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import  messages

from authapp.models import User
from adminapp.forms import AdminUserCreationForm


# Create your views here.

def index(request):
    return render(request, 'adminapp/admin.html')


def create_user(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Пользователь создан')
            return redirect('admin-staff:users')
    else:
        form = AdminUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin-users-create.html', context)


def change_user(request, user_id):
    return render(request, 'adminapp/admin-users-update-delete.html')


def users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)
