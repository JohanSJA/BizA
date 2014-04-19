from django.contrib import admin

from .models import Store, Salesperson, RetailSales, RetailSalesLine


class SalespersonInline(admin.StackedInline):
    model = Salesperson


class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "telephone"]
    inlines = [SalespersonInline]


class RetailSalesLineInline(admin.TabularInline):
    model = RetailSalesLine


class RetailSalesAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "store", "salesperson", "closed_at"]
    inlines = [RetailSalesLineInline]


admin.site.register(Store, StoreAdmin)
admin.site.register(RetailSales, RetailSalesAdmin)
