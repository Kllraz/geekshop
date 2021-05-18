from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from authapp.models import User
from adminapp.forms import AdminUserCreationForm, AdminUserEditForm


# Create your views here.

def index(request):
    return render(request, 'adminapp/admin.html')


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


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()

    messages.success(request, 'Пользователь удален')

    return redirect('admin-staff:users')


def users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)
