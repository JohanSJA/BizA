from django import forms
from django.forms.models import inlineformset_factory

from stocks.models import Log

from .models import *


class SaleCloseForm(forms.ModelForm):
    amount_paid = forms.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        model = Sale
        fields = []

    def clean(self):
        errors = []

        cleaned_data = super().clean()
        sale = self.instance

        amount_paid = self.cleaned_data['amount_paid']
        if amount_paid < sale.total_price():
            errors.append(forms.ValidationError('Amount paid is too low.'))

        for line in sale.line_set.all():
            log = Log.objects.filter(
                    warehouse=sale.shop.warehouse,
                    stock=line.stock).first()
            if log:
                if log.balance() < line.quantity:
                    errors.append(forms.ValidationError('Not enough {} for sale.'.format(line.stock)))
            else:
                errors.append(forms.ValidationError('Not {} in warehouse.'.format(line.stock)))

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data


SaleLineFormSet = inlineformset_factory(Sale, Line)
