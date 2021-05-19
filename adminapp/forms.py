from authapp.forms import RegisterForm, EditForm
from authapp.models import User
from mainapp.models import Product, ProductCategory

from django import forms


class AdminUserCreationForm(RegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')


class AdminUserEditForm(EditForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4'
    }))


class AdminProductEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
    }))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
    }, ))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(),
                                      widget=forms.Select(attrs={
                                          'class': 'form-select',
                                      }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'category', 'image')
