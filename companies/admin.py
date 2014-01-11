from django.contrib import admin

from companies.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'reg_num', 'address']


admin.site.register(Company, CompanyAdmin)
