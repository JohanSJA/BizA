from django.contrib import admin

from warehouses.models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location')


admin.site.register(Warehouse, WarehouseAdmin)
