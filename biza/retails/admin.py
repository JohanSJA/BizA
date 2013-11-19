from django.contrib import admin

from .models import *

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'warehouse']

class SaleLineInline(admin.TabularInline):
    model = SaleLine

class SaleAdmin(admin.ModelAdmin):
    list_display = ['store', 'get_status', 'opening_time', 'closing_time', 'quoting_time', 'total_amount']
    inlines = [SaleLineInline,]
    fieldsets = (
        ('General', {
            'fields': ('store', 'saleperson', 'opened_by')
        }),
        ('Closing', {
            'fields': ('cash_bill_number', 'closing_time', 'closed_by')
        }),
        ('Quoting', {
            'fields': ('quotation_number', 'quoting_time', 'quoted_by')
        })
    )

admin.site.register(Store, StoreAdmin)
admin.site.register(Saleperson)
admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleLine)
