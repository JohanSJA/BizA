from django.contrib import admin

from .models import *


class ComponentInline(admin.TabularInline):
    model = Component
    fk_name = 'stock'


class StockAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'uom', 'is_package', 'discontinued']
    list_filter = ['discontinued']
    inlines = [ComponentInline]


class LogInline(admin.TabularInline):
    model = Log


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    inlines = [LogInline]


class EntryInline(admin.TabularInline):
    model = Entry


class LogAdmin(admin.ModelAdmin):
    list_display = ['warehouse', 'stock']
    list_filter = ['warehouse', 'stock']
    inlines = [EntryInline]


admin.site.register(Uom)
admin.site.register(Stock, StockAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Log, LogAdmin)
