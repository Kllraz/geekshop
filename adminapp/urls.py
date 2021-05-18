from django.urls import path

from adminapp.views import index, create_user, change_user, users, delete_user

app_name = 'authapp'

urlpatterns = [
    path('', index, name='index'),
    path('user-create/', create_user, name='create_user'),
    path('users/', users, name='users'),
    path('user-change/<int:user_id>/', change_user, name='change_user'),
    path('user-delete_user/<int:user_id>/', delete_user, name='delete_user'),
]
