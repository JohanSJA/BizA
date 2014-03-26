from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category']
    list_filter = ['category']
    search_fields = ['code', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
