from django import forms

from .models import *


class PackageItemForm(forms.ModelForm):
    class Meta:
        model = PackageItem
        fields = ['item', 'quantity']


class PackageInfoForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['model', 'name', 'barcode']


class PackagePriceForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['retail_price', 'lowest_retail_price', 'wholesale_price', 'lowest_wholesale_price']


class ItemQuantityForm(forms.ModelForm):
    REASONS = (
        ('T', 'Transfers'),
        ('R', 'Spare part for repair'),
        ('O', 'Own use'),
    )

    reason = forms.ChoiceField(choices=REASONS)

    class Meta:
        model = ItemQuantity
        fields = ['warehouse', 'quantity', 'reason']


class ItemQuantityStoreForm(ItemQuantityForm):
    class Meta:
        model = ItemQuantity
        fields = ['quantity', 'reason']
