from django.contrib import admin

from products.models import Unit, Product, Component


class ComponentInline(admin.TabularInline):
    model = Component
    fk_name = 'product'

class ProductAdmin(admin.ModelAdmin):
    inlines = (ComponentInline, )


admin.site.register(Unit)
admin.site.register(Product, ProductAdmin)
