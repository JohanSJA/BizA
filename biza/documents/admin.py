from django.contrib import admin

from .models import *


class VersionInline(admin.StackedInline):
    model = Version


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'prefix', 'length', 'version']
    inlines = [VersionInline]


class VersionAdmin(admin.ModelAdmin):
    list_display = ['document', 'get_full_name', 'get_next']


admin.site.register(Document, DocumentAdmin)
admin.site.register(Version, VersionAdmin)
