from django.forms.models import inlineformset_factory

from .models import *


PartnerLocationFormSet = inlineformset_factory(Partner, Location)
SaleSaleLineFormSet = inlineformset_factory(Sale, SaleLine)
PurchasePurchaseLineFormSet = inlineformset_factory(Purchase, PurchaseLine)
