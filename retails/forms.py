from django import forms
from django.forms.models import inlineformset_factory

from stocks.models import Stock

from .models import *


class SaleCloseForm(forms.ModelForm):
    amount_paid = forms.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        model = Sale
        fields = []

    def clean(self):
        cleaned_data = super(SaleCloseForm, self).clean()
        sale = self.instance

        amount_paid = self.cleaned_data['amount_paid']
        if amount_paid < sale.total_price():
            raise forms.ValidationError('Amount paid is too low.')

        return cleaned_data


SaleLineFormSet = inlineformset_factory(Sale, Line)
