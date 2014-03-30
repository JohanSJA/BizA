from django.shortcuts import render
from django.contrib.formtools.wizard.views import SessionWizardView

from .forms import (
    PartnerForm, AddressForm, ContactMethodForm,
    SupplierForm, CustomerForm
)


class PartnerWizardView(SessionWizardView):
    form_list = [PartnerForm, AddressForm, ContactMethodForm,
            SupplierForm, CustomerForm]

    def done(self, form_list, **kwargs):
        return render(self.request, 'base.html')
