from django.contrib import admin

from .models import *


class BalanceInline(admin.TabularInline):
    model = Balance


class StockAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'unit']
    inlines = [BalanceInline]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


admin.site.register(Unit)
admin.site.register(Stock, StockAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
