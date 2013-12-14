from django.forms import ModelForm

from products.models import Component, Quantity


class ComponentForm(ModelForm):
    class Meta:
        model = Component
        fields = ['component', 'quantity']

class QuantityForm(ModelForm):
    class Meta:
        model = Quantity
        fields = ['warehouse', 'changes']
