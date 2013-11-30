from django.contrib import admin

from products.models import Unit, Category, Product, Component, BasePrice, BranchPrice


class ComponentInline(admin.TabularInline):
    model = Component
    fk_name = 'product'

class BasePriceInline(admin.StackedInline):
    model = BasePrice
    can_delete = False
    verbose_name_plural = 'base price'

class BranchPriceInline(admin.StackedInline):
    model = BranchPrice

class ProductAdmin(admin.ModelAdmin):
    inlines = (ComponentInline, BasePriceInline, BranchPriceInline)


admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
