from django.contrib import admin

from .models import Partner, Address, ContactMethod


class AddressInline(admin.TabularInline):
    model = Address


class ContactMethodInline(admin.TabularInline):
    model = ContactMethod


class PartnerAdmin(admin.ModelAdmin):
    inlines = [ContactMethodInline, AddressInline]


admin.site.register(Partner, PartnerAdmin)
