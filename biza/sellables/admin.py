from django.contrib import admin

from sellables.models import Unit, TaxConstant, Category, Sellable


admin.site.register(Unit)
admin.site.register(TaxConstant)
admin.site.register(Category)
admin.site.register(Sellable)
