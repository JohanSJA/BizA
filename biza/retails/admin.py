from django.contrib import admin

from retails.models import Drawer, Session


class SessionInline(admin.TabularInline):
    model = Session

class DrawerAdmin(admin.ModelAdmin):
    list_display = ('branch', 'name')
    inlines = (SessionInline,)


admin.site.register(Drawer, DrawerAdmin)
