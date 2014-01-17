from django.contrib import admin

from .models import *


class WorkerInline(admin.TabularInline):
    model = Worker


class ShopAdmin(admin.ModelAdmin):
    inlines = [WorkerInline]


class PriceAdmin(admin.ModelAdmin):
    list_display = ['stock', 'base', 'lowest']


class LineInline(admin.TabularInline):
    model = Line


class ReceiptInline(admin.TabularInline):
    model = Receipt


class SaleAdmin(admin.ModelAdmin):
    list_display = ['shop', 'closed_at', 'closed_by']
    list_filter = ['shop']
    inlines = [ReceiptInline, LineInline]


admin.site.register(Shop, ShopAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Sale, SaleAdmin)
