from django.forms.models import inlineformset_factory

from .models import *


PartnerLocationFormSet = inlineformset_factory(Partner, Location, extra=1)


SaleSaleLineFormSet = inlineformset_factory(Sale, SaleLine, extra=5)


PurchasePurchaseLineFormSet = inlineformset_factory(Purchase, PurchaseLine,
        extra=5)

PurchasePurchaseOrderFormSet = inlineformset_factory(Purchase, PurchaseOrder, extra=1)
