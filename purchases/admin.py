from django.contrib import admin

from .models import (
    Supplier, PurchaseOrder, PurchaseOrderLine, Invoice, InvoiceLine,
    DeliveryOrder, DeliveryOrderLine
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ["code", "partner"]


class PurchaseOrderLineInline(admin.TabularInline):
    model = PurchaseOrderLine


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "supplier", "issuing_date", "total_price"]
    inlines = [PurchaseOrderLineInline]


class InvoiceLineInline(admin.TabularInline):
    model = InvoiceLine


class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number", "supplier", "issuing_date", "payment_due_date",
        "payment_made_date", "total_price"
    ]
    inlines = [InvoiceLineInline]


class DeliveryOrderLineInline(admin.TabularInline):
    model = DeliveryOrderLine


class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number", "supplier", "issuing_date", "good_received_date",
        "total_quantity"
    ]
    inlines = [DeliveryOrderLineInline]


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(DeliveryOrder, DeliveryOrderAdmin)
