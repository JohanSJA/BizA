from django.contrib import admin

from .models import *


class StockAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'unit']


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class BalanceAdmin(admin.ModelAdmin):
    list_display = ['stock', 'warehouse', 'changes', 'reason', 'amount']
    list_filter = ['stock', 'warehouse', 'reason']


admin.site.register(Unit)
admin.site.register(Stock, StockAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Balance, BalanceAdmin)
