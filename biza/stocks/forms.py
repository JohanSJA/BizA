from django import forms

from .models import *


class PackageItemForm(forms.ModelForm):
    class Meta:
        model = PackageItem
        fields = ['item', 'quantity']
