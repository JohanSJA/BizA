from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category']
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
