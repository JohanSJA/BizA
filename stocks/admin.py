from django.contrib import admin

from products.models import Product
from products.admin import ProductAdmin

from .models import Uom, Stock, Warehouse, Log, LogEntry


class UomAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class StockInline(admin.StackedInline):
    model = Stock


class ProductAdminWithInlines(ProductAdmin):
    inlines = [StockInline,]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class LogEntryInline(admin.TabularInline):
    model = LogEntry


class LogAdmin(admin.ModelAdmin):
    list_display = ['stock', 'warehouse', 'total_amount']
    list_filter = ['stock', 'warehouse']
    inlines = [LogEntryInline,]


admin.site.register(Uom, UomAdmin)
admin.site.unregister(Product)
admin.site.register(Product, ProductAdminWithInlines)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Log, LogAdmin)
