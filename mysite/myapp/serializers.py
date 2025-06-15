from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'productcode', 'description', 'price', 'stock', 'category', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'date', 'total']
        read_only_fields = ['date']