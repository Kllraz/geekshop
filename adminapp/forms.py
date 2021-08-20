from authapp.forms import RegisterForm, EditForm
from authapp.models import User
from mainapp.models import Product, ProductCategory

from django import forms

from ordersapp.models import Order, OrderItem


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
        'min': 0
    }))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
        'min': 0
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


class AdminCreateProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите название'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите описание'
    }))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите цену',
        'min': 0
    }))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите количество',
        'min': 0
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


class AdminCreateProductCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите название'
    }))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите описание'
    }))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class AdminEditProductCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'
    }))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control py-4'
    }))

    discount = forms.IntegerField(label='скидка', required=False, min_value=0, max_value=90, initial=0,
                                  widget=forms.NumberInput(attrs={
                                      'class': 'form-control py-4'
                                  }))

    class Meta:
        model = ProductCategory
        # fields = ('name', 'description', 'discount')
        exclude = ()


class AdminEditOrderForm(forms.ModelForm):
    status = forms.CharField(max_length=3, widget=forms.Select(choices=Order.ORDER_STATUS_CHOICES,
                                                               attrs={
                                                                   'class': 'form-control',
                                                               }))

    class Meta:
        model = Order
        fields = ('status',)
