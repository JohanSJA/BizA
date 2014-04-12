from django.contrib import admin

from .models import Pricelist, PricelistEntry


class PricelistEntryInline(admin.TabularInline):
    model = PricelistEntry


class PricelistAdmin(admin.ModelAdmin):
    inlines = [PricelistEntryInline]


admin.site.register(Pricelist, PricelistAdmin)
