from django.forms.models import inlineformset_factory

from .models import *


SaleSaleLineFormSet = inlineformset_factory(Sale, SaleLine)
PurchasePurchaseLineFormSet = inlineformset_factory(Purchase, PurchaseLine)
