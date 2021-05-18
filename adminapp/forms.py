from authapp.forms import RegisterForm
from authapp.models import User

from django import forms


class AdminUserCreationForm(RegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')
