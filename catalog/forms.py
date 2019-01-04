from .models import Product
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('is_active', 'is_visibility','price','quantity','sku','product_id')