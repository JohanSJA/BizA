from django.contrib import admin

from uoms.models import Uom


class UomAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


admin.site.register(Uom, UomAdmin)
