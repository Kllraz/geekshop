from django.urls import path

from adminapp.views import index, create_user, change_user, users, delete_user, activate_user

app_name = 'authapp'

urlpatterns = [
    path('', index, name='index'),
    path('user-create/', create_user, name='create_user'),
    path('users/', users, name='users'),
    path('user-change/<int:user_id>/', change_user, name='change_user'),
    path('user-delete/<int:user_id>/', delete_user, name='delete_user'),
    path('user-activate/<int:user_id>/', activate_user, name='activate_user'),
]
