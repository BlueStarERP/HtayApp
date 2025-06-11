from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'barcodeid', 'description', 'price', 'stock', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'barcodeid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter barcode ID'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter stock quantity'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
