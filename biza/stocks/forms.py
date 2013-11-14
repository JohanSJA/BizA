from django import forms

from .models import *


class PackageForm1(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['model', 'name', 'barcode']


class PackageForm2(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['retail_price', 'lowest_retail_price',
                  'wholesale_price', 'lowest_wholesale_price']
