from django.contrib import admin

from .models import Uom, Product, Warehouse, Log, LogEntry


class UomAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'description']
    list_filter = ['category']
    search_fields = ['code', 'name']


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class LogEntryInline(admin.TabularInline):
    model = LogEntry


class LogAdmin(admin.ModelAdmin):
    list_display = ['product', 'warehouse', 'total_amount']
    list_filter = ['product', 'warehouse']
    inlines = [LogEntryInline,]


admin.site.register(Uom, UomAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Log, LogAdmin)
