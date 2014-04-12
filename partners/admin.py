from django.contrib import admin

from .models import Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ["name", "telephone", "fax", "email"]


admin.site.register(Partner, PartnerAdmin)
