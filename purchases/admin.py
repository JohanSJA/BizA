from django.contrib import admin

from .models import (
    Supplier, PurchaseOrder, PurchaseOrderLine,
    PurchaseInvoice, PurchaseInvoiceLine,
    PurchaseDeliveryOrder, PurchaseDeliveryOrderLine
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ["code", "partner"]


class PurchaseOrderLineInline(admin.TabularInline):
    model = PurchaseOrderLine


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "supplier", "issuing_date", "total_price"]
    inlines = [PurchaseOrderLineInline]


class PurchaseInvoiceLineInline(admin.TabularInline):
    model = PurchaseInvoiceLine


class PurchaseInvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number", "supplier", "issuing_date", "payment_due_date",
        "payment_made_date", "total_price"
    ]
    inlines = [PurchaseInvoiceLineInline]


class PurchaseDeliveryOrderLineInline(admin.TabularInline):
    model = PurchaseDeliveryOrderLine


class PurchaseDeliveryOrderAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number", "supplier", "issuing_date", "good_received_date",
        "total_quantity"
    ]
    inlines = [PurchaseDeliveryOrderLineInline]


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(PurchaseInvoice, PurchaseInvoiceAdmin)
admin.site.register(PurchaseDeliveryOrder, PurchaseDeliveryOrderAdmin)
