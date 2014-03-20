from django.contrib import admin

from .models import Uom


class UomAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


admin.site.register(Uom, UomAdmin)
