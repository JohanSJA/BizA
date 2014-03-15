from django.contrib import admin

from .models import PriceList, Price


class PriceInline(admin.TabularInline):
    model = Price


class PriceListAdmin(admin.ModelAdmin):
    inlines = [PriceInline,]


admin.site.register(PriceList, PriceListAdmin)
