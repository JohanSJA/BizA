from django.contrib import admin

from .models import *

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'warehouse']

class SaleLineInline(admin.TabularInline):
    model = SaleLine

class SaleAdmin(admin.ModelAdmin):
    list_display = ['store', 'opening_time', 'closing_time', 'total_amount']
    inlines = [SaleLineInline,]

admin.site.register(Store, StoreAdmin)
admin.site.register(Saleperson)
admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleLine)
