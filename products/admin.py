from django.contrib import admin

from .models import Category, Uom, Product, Warehouse, Log, LogEntry


class UomAdmin(admin.ModelAdmin):
    list_display = ["name", "abbreviation"]


class LogInline(admin.TabularInline):
    model = Log


class ProductAdmin(admin.ModelAdmin):
    list_display = ["model", "category", "uom", "balance"]
    list_filter = ["category"]
    inlines = [LogInline]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "balance"]
    inlines = [LogInline]


class LogEntryInline(admin.TabularInline):
    model = LogEntry


class LogAdmin(admin.ModelAdmin):
    list_display = ["product", "warehouse", "balance"]
    list_filter = ["product", "warehouse"]
    inlines = [LogEntryInline]


admin.site.register(Category)
admin.site.register(Uom, UomAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Log, LogAdmin)
