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
            'name': forms.TextInput(attrs={'class': '', 'placeholder': 'Enter product name'}),
            'barcodeid': forms.TextInput(attrs={'class': '', 'placeholder': 'Enter barcode ID'}),
            'description': forms.Textarea(attrs={'class': '', 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': '', 'placeholder': 'Enter price'}),
            'stock': forms.NumberInput(attrs={'class': '', 'placeholder': 'Enter stock quantity'}),
            'category': forms.Select(attrs={'class': ''}),
            # 'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'productcode', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'productcode': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'price': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'category':forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        }