from django.contrib import admin

from .models import *


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['shop', 'worker']
    list_filter = ['shop']


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


admin.site.register(Shop)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Sale, SaleAdmin)
