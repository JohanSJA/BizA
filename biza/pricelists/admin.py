from django.contrib import admin

from pricelists.models import Pricelist


class PricelistAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Pricelist, PricelistAdmin)
