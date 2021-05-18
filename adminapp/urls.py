from django.urls import path

from adminapp.views import index, create_user, change_user, users

app_name = 'authapp'

urlpatterns = [
    path('', index, name='index'),
    path('user-create/', create_user, name='create_user'),
    path('users/', users, name='users'),
    path('user-change/<int:user_id>/', change_user, name='change_user'),
]
