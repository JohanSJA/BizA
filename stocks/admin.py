from django.contrib import admin

from .models import Uom, Stock, Warehouse, Log, LogEntry


class UomAdmin(admin.ModelAdmin):
    list_display = ["name", "abbreviation"]


class LogInline(admin.TabularInline):
    model = Log


class StockAdmin(admin.ModelAdmin):
    list_display = ["product", "uom", "balance"]
    inlines = [LogInline]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "balance"]
    inlines = [LogInline]


class LogEntryInline(admin.TabularInline):
    model = LogEntry


class LogAdmin(admin.ModelAdmin):
    list_display = ["stock", "warehouse", "balance"]
    list_filter = ["stock", "warehouse"]
    inlines = [LogEntryInline]


admin.site.register(Uom, UomAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Log, LogAdmin)
