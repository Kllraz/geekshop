import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import User, UserProfile
from authapp.validators import minNameLength


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Введите имя пользователя'
    }), validators=[minNameLength])
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Введите адрес эл. почты'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Введите имя'
    }), validators=[minNameLength])
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Введите фамилию'
    }), validators=[minNameLength])
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save()
        user.is_active = False

        salt = hashlib.sha1(str(random.random()).encode('UTF-8')).hexdigest()[:6]
        activation_code = hashlib.sha1((salt + user.email).encode('UTF-8')).hexdigest()

        user.activation_key = activation_code
        user.save()

        return user


class EditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'readOnly': True,
    }), validators=[minNameLength])
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-2',
        'readOnly': True,
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
    }), validators=[minNameLength])
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
    }), validators=[minNameLength])
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control py-2',
        'type': 'date'
    }, format='%Y-%m-%d'))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'birthday')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('tagline', 'gender', 'about_me')

    tagline = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
    }), required=False)

    about_me = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-2',
        'rows': 3,
    }), required=False)

    gender = forms.CharField(max_length=1, widget=forms.Select(choices=UserProfile.GENDER_CHOICE,
                                                               attrs={
                                                                   'class': 'form-control',
                                                               }))
