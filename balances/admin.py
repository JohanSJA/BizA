from django.contrib import admin

from .models import Warehouse, BalanceLog, BalanceLogEntry


class BalanceLogInline(admin.TabularInline):
    model = BalanceLog


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["name", "balance"]
    inlines = [BalanceLogInline]


class BalanceLogEntryInline(admin.TabularInline):
    model = BalanceLogEntry


class BalanceLogAdmin(admin.ModelAdmin):
    list_display = ["product", "warehouse", "total_amount"]
    list_filter = ["product", "warehouse"]
    inlines = [BalanceLogEntryInline]


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(BalanceLog, BalanceLogAdmin)
