from django import forms
from django.forms.models import inlineformset_factory

from stocks.models import Warehouse

from .models import *


PartnerLocationFormSet = inlineformset_factory(Partner, Location, extra=1)


SaleSaleLineFormSet = inlineformset_factory(Sale, SaleLine, extra=5)


PurchasePurchaseLineFormSet = inlineformset_factory(Purchase, PurchaseLine,
        extra=5)


class PurchasePlaceOrderForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = []


class PurchaseInvoiceForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(Warehouse.objects.all())

    class Meta:
        model = PurchaseInvoice
        fields = ['number']



SalePlaceOrderForm = inlineformset_factory(Sale, SaleOrder)


SaleSaleDeliveryFormSet = inlineformset_factory(Sale, SaleDelivery)
