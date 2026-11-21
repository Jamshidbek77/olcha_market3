from django import forms
from .models import Shop, Product, User


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['turi', 'name', 'price', 'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['user', 'shop']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']