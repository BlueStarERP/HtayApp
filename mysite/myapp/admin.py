from django.contrib import admin
from .models import Category, Product
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
