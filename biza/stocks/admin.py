from django.contrib import admin

from .models import *


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']


class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

class ItemQuantityInline(admin.TabularInline):
    model = ItemQuantity


class ItemAdmin(admin.ModelAdmin):
    list_display = ['model', 'name', 'barcode', 'retail_price', 'wholesale_price', 'cost_price']
    inlines = [ItemQuantityInline,]


class PackageItemInline(admin.TabularInline):
    model = PackageItem


class PackageAdmin(admin.ModelAdmin):
    list_display = ['model', 'name', 'barcode', 'retail_price', 'separate_retail_price', 'wholesale_price', 'separate_wholesale_price', 'cost_price']
    inlines = [PackageItemInline,]


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(UnitOfMeasure, UnitOfMeasureAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Package, PackageAdmin)
