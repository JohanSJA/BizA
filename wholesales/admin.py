from django.contrib import admin

from .models import (
    Customer, SalesOrder, SalesOrderLine,
    SalesInvoice, SalesInvoiceLine,
    SalesDeliveryOrder, SalesDeliveryOrderLine
)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["code", "partner"]


class SalesOrderLineInline(admin.TabularInline):
    model = SalesOrderLine


class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "customer", "issuing_date", "total_price"]
    inlines = [SalesOrderLineInline]


class SalesInvoiceLineInline(admin.TabularInline):
    model = SalesInvoiceLine


class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number", "customer", "issuing_date", "payment_due_date",
        "payment_received_date", "total_price"
    ]
    inlines = [SalesInvoiceLineInline]


class SalesDeliveryOrderLineInline(admin.TabularInline):
    model = SalesDeliveryOrderLine


class SalesDeliveryOrderAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number", "customer", "issuing_date", "good_sent_date",
        "total_quantity"
    ]
    inlines = [SalesDeliveryOrderLineInline]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(SalesInvoice, SalesInvoiceAdmin)
admin.site.register(SalesDeliveryOrder, SalesDeliveryOrderAdmin)
