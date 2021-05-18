from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'adminapp/admin.html')


def create_user(request):
    return render(request, 'adminapp/admin-users-create.html')


def change_user(request, user_id):
    return render(request, 'adminapp/admin-users-update-delete.html')


def users(request):
    return render(request, 'adminapp/admin-users-read.html')
