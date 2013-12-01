from django.contrib import admin

from products.models import Unit, Product, Component, Warehouse, Quantity


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

class ComponentInline(admin.TabularInline):
    model = Component
    fk_name = 'product'

class QuantityInline(admin.TabularInline):
    model = Quantity

class ProductAdmin(admin.ModelAdmin):
    inlines = (ComponentInline, QuantityInline)


admin.site.register(Unit)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Product, ProductAdmin)
