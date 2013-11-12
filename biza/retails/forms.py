from django import forms

from .models import *


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['saleperson']


class SaleCloseForm(forms.ModelForm):
    amount_paid = forms.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        model = Sale
        fields = []


class SaleQuoteForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = []
