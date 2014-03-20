from django.contrib import admin

from .models import Uom, Category, Product


class UomAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'uom']
    list_filter = ['category']


admin.site.register(Uom, UomAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
