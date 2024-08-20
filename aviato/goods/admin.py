from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'created', 'updated', 'available')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    list_editable = ('price', 'available')
    search_fields = ('name', 'category__name')
