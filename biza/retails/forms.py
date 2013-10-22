from django.forms import ModelForm

from .models import *


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['saleperson']
