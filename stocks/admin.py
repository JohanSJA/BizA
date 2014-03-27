from django.contrib import admin

from products.models import Product
from products.admin import ProductAdmin

from .models import Uom, ProductUom, Warehouse, Log, LogEntry


class UomAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class ProductUomInline(admin.StackedInline):
    model = ProductUom


class ProductAdminWithInlines(ProductAdmin):
    inlines = [ProductUomInline,]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class LogEntryInline(admin.TabularInline):
    model = LogEntry


class LogAdmin(admin.ModelAdmin):
    list_display = ['product', 'warehouse', 'total_amount']
    list_filter = ['product', 'warehouse']
    inlines = [LogEntryInline,]


admin.site.register(Uom, UomAdmin)
admin.site.unregister(Product)
admin.site.register(Product, ProductAdminWithInlines)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Log, LogAdmin)
