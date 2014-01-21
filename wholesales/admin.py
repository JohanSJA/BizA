from django.contrib import admin

from .models import *


class PriceAdmin(admin.ModelAdmin):
    list_display = ['stock', 'base', 'lowest', 'updated_at']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']


class PurchaseLineInline(admin.TabularInline):
    model = PurchaseLine


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['partner', 'doc_num', 'date', 'total_price']
    list_filter = ['partner']
    inlines = [PurchaseLineInline]


class SaleLineInline(admin.TabularInline):
    model = SaleLine


class SaleAdmin(admin.ModelAdmin):
    list_display = ['partner', 'doc_num', 'date', 'total_price']
    list_filter = ['partner']
    inlines = [SaleLineInline]


admin.site.register(Price, PriceAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Term)
admin.site.register(Sale, SaleAdmin)
