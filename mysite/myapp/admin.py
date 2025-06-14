from django.contrib import admin
from .models import Category, Product, Cart, CartItem
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'barcodeid', 'price', 'stock', 'category')
    search_fields = ('name', 'barcodeid')
    list_filter = ('category',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'date', 'created_at', 'updated_at')
    search_fields = ('date',)
    readonly_fields = ('created_at', 'updated_at')



class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'price')
    search_fields = ('cart__id', 'product__name')
    list_filter = ('cart', 'product')
    
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
