from django import forms
from django.forms.models import inlineformset_factory

from .models import *


StockComponentFormSet = inlineformset_factory(Stock, Component, fk_name='stock')


class StockCodePrintForm(forms.Form):
    start = forms.IntegerField(max_value=25, min_value=1, label='Starting sticker',
            help_text='Number is counted from top to bottom and left to right.')
    amount = forms.IntegerField(min_value=1, label='Total amount',
            help_text='Amount that you want to print.')
