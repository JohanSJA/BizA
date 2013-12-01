from django.contrib import admin

from retails.models import Branch, Employee, Price


class EmployeeInline(admin.StackedInline):
    model = Employee

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (EmployeeInline,)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('branch', 'product', 'cost', 'base', 'lowest')
    list_filter = ('branch', 'product')


admin.site.register(Branch, BranchAdmin)
admin.site.register(Price, PriceAdmin)
