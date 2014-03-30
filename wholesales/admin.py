from django.contrib import admin

from .models import Salesman, Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['partner', 'code', 'served_by']


admin.site.register(Salesman)
admin.site.register(Customer, CustomerAdmin)
