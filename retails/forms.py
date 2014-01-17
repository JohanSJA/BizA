from django import forms

from .models import *


class SaleCloseForm(forms.ModelForm):
    amount_paid = forms.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        model = Sale
        fields = []
