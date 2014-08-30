from django.contrib import admin

from .models import Category, Uom, Product


class UomAdmin(admin.ModelAdmin):
    list_display = ["name", "abbreviation"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["model", "category"]
    list_filter = ["category"]


admin.site.register(Category)
admin.site.register(Uom, UomAdmin)
admin.site.register(Product, ProductAdmin)
