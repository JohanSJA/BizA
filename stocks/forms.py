from django import forms

from .models import Warehouse


class ProductLogForm(forms.Form):
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all())
    quantity_adjustment = forms.IntegerField(help_text="Positive value for stock increase. Negative value for stock decrease.")
    description = forms.CharField(max_length=100, help_text="Reason for this stock changes to happen.")
