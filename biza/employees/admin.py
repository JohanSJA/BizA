from django.contrib import admin

from employees.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'admission_date', 'registry_number')


admin.site.register(Employee, EmployeeAdmin)
