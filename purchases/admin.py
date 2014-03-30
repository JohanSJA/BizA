from django.contrib import admin

from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['partner', 'code']


admin.site.register(Supplier, SupplierAdmin)
