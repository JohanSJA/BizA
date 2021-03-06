from django import forms

from .models import Pricelist


class PricelistForm(forms.ModelForm):
    base = forms.ModelChoiceField(queryset=Pricelist.objects.filter(base=None), required=False)

    class Meta:
        model = Pricelist
        fields = "__all__"
