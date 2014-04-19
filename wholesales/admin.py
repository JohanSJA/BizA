from django.contrib import admin

from .models import (
    Customer, SalesOrder, SalesOrderLine,
    SalesDeliveryOrder, SalesDeliveryOrderLine
)


class SalesOrderLineInline(admin.TabularInline):
    model = SalesOrderLine


class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "issuing_date", "total_price"]
    inlines = [SalesOrderLineInline]


class SalesDeliveryOrderLineInline(admin.TabularInline):
    model = SalesDeliveryOrderLine


class SalesDeliveryOrderAdmin(admin.ModelAdmin):
    list_display = [
        "id", "customer", "issuing_date", "good_sent_date",
        "total_quantity"
    ]
    inlines = [SalesDeliveryOrderLineInline]


admin.site.register(Customer)
admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(SalesDeliveryOrder, SalesDeliveryOrderAdmin)
