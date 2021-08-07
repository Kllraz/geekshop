from django.urls import path

from authapp.views import UserLoginView, UserLogout, UserUpdateView, UserCreateView, verify

app_name = 'authapp'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('register', UserCreateView.as_view(), name='register'),
    path('logout', UserLogout.as_view(), name='logout'),
    path('profile', UserUpdateView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activation_key>', verify, name='verify')
]
