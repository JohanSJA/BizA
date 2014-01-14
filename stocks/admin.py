from django.contrib import admin

from .models import *


class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class StockAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'unit']


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class BalanceAdmin(admin.ModelAdmin):
    list_display = ['stock', 'warehouse', 'changes', 'amount']
    list_filter = ['warehouse']


admin.site.register(Unit, UnitAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Balance, BalanceAdmin)
