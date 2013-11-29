from django.contrib import admin

from cashbooks.models import Cashbook


class CashbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Cashbook, CashbookAdmin)
