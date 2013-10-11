from django.contrib import admin

from .models import *

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'warehouse']
    
class SaleLineInline(admin.TabularInline):
    model = SaleLine

class SaleAdmin(admin.ModelAdmin):
    list_display = ['store', 'open_time', 'closing_time', 'total_amount']
    inlines = [SaleLineInline,]

admin.site.register(Store, StoreAdmin)
admin.site.register(Saleperson)
admin.site.register(Sale, SaleAdmin)
