from django.contrib import admin

from .models import (
    Category, Uom, Product, Pricelist, PricelistEntry,
    Warehouse, BalanceLog, BalanceLogEntry
)


class UomAdmin(admin.ModelAdmin):
    list_display = ["name", "abbreviation"]


class BalanceLogInline(admin.TabularInline):
    model = BalanceLog


class ProductAdmin(admin.ModelAdmin):
    list_display = ["model", "category"]
    list_filter = ["category"]


class PricelistEntryInline(admin.TabularInline):
    model = PricelistEntry


class PricelistAdmin(admin.ModelAdmin):
    list_display = ["name", "base"]
    inlines = [PricelistEntryInline]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["name", "balance"]
    inlines = [BalanceLogInline]


class BalanceLogEntryInline(admin.TabularInline):
    model = BalanceLogEntry


class BalanceLogAdmin(admin.ModelAdmin):
    list_display = ["product", "warehouse", "total_amount"]
    list_filter = ["product", "warehouse"]
    inlines = [BalanceLogEntryInline]


admin.site.register(Category)
admin.site.register(Uom, UomAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Pricelist, PricelistAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(BalanceLog, BalanceLogAdmin)
