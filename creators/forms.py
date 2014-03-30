from django import forms

from partners.models import Partner, Address, ContactMethod
from purchases.models import Supplier
from wholesales.models import Customer


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['partner']


class ContactMethodForm(forms.ModelForm):
    class Meta:
        model = ContactMethod
        exclude = ['partner']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ['partner']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['partner']
