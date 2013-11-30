from django.contrib import admin

from tills.models import Till, Entry


class EntryInline(admin.TabularInline):
    model = Entry

class TillAdmin(admin.ModelAdmin):
    list_display = ('station', 'opening_time')
    inlines = (EntryInline,)


admin.site.register(Till, TillAdmin)
