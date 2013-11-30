from django.contrib import admin

from branches.models import Branch, Employee


class EmployeeInline(admin.StackedInline):
    model = Employee

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (EmployeeInline,)


admin.site.register(Branch, BranchAdmin)
