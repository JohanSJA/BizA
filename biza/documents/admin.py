from django.contrib import admin

from .models import *


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'prefix', 'length', 'number', 'get_full_name']


admin.site.register(Document, DocumentAdmin)
