from django.contrib import admin

from branches.models import Branch, Station


class StationInline(admin.TabularInline):
    model = Station

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    inlines = (StationInline,)


admin.site.register(Branch, BranchAdmin)
