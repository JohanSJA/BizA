from django.contrib import admin

from .models import (
    Supplier, PurchaseOrder, PurchaseOrderLine,
    PurchaseDeliveryOrder, PurchaseDeliveryOrderLine
)


class PurchaseOrderLineInline(admin.TabularInline):
    model = PurchaseOrderLine


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["id","supplier", "issuing_date", "total_price"]
    inlines = [PurchaseOrderLineInline]


class PurchaseDeliveryOrderLineInline(admin.TabularInline):
    model = PurchaseDeliveryOrderLine


class PurchaseDeliveryOrderAdmin(admin.ModelAdmin):
    list_display = [
        "id", "supplier", "issuing_date", "good_received_date",
        "total_quantity"
    ]
    inlines = [PurchaseDeliveryOrderLineInline]


admin.site.register(Supplier)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(PurchaseDeliveryOrder, PurchaseDeliveryOrderAdmin)
