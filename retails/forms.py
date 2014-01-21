from django import forms
from django.forms.models import inlineformset_factory

from stocks.models import Stock

from .models import *


class SaleCloseForm(forms.ModelForm):
    amount_paid = forms.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        model = Sale
        fields = []


SaleLineFormSet = inlineformset_factory(Sale, Line)
