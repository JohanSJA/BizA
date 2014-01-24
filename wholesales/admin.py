from django.contrib import admin

from .models import *


class PriceAdmin(admin.ModelAdmin):
    list_display = ['stock', 'base', 'lowest', 'updated_at']


class LocationInline(admin.TabularInline):
    model = Location


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    inlines = [LocationInline]


class PurchaseOrderInline(admin.TabularInline):
    model = PurchaseOrder


class PurchaseInvoiceInline(admin.TabularInline):
    model = PurchaseInvoice


class PurchaseLineInline(admin.TabularInline):
    model = PurchaseLine


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['partner', 'total_price']
    list_filter = ['partner']
    inlines = [PurchaseOrderInline, PurchaseInvoiceInline, PurchaseLineInline]


class SaleOrderInline(admin.TabularInline):
    model = SaleOrder


class SaleLineInline(admin.TabularInline):
    model = SaleLine


class SaleAdmin(admin.ModelAdmin):
    list_display = ['partner', 'total_price']
    list_filter = ['partner']
    inlines = [SaleOrderInline, SaleLineInline]


admin.site.register(Price, PriceAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Term)
admin.site.register(Sale, SaleAdmin)
