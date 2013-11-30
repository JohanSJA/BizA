from django.contrib import admin

from branches.models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')


admin.site.register(Branch, BranchAdmin)
