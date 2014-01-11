from django.contrib import admin

from retails.models import Branch, Employee, Price, Sale, SaleLine


class EmployeeInline(admin.StackedInline):
    model = Employee

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (EmployeeInline,)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('branch', 'product', 'cost', 'base', 'lowest')
    list_filter = ('branch', 'product')

class SaleLineInline(admin.TabularInline):
    model = SaleLine

class SaleAdmin(admin.ModelAdmin):
    list_display = ('branch', 'handled_by', 'opening_time', 'opened_by')
    inlines = (SaleLineInline,)


admin.site.register(Branch, BranchAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Sale, SaleAdmin)
