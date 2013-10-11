from django.contrib import admin

from .models import *

class PackageItemInline(admin.TabularInline):
    model = PackageItem

class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageItemInline,]

admin.site.register(Item)
admin.site.register(Package, PackageAdmin)
