from django.shortcuts import redirect
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib import messages

from .forms import (
    PartnerForm, AddressForm, ContactMethodForm,
    SupplierForm, CustomerForm
)


class PartnerWizardView(SessionWizardView):
    form_list = [PartnerForm, AddressForm, ContactMethodForm,
            SupplierForm, CustomerForm]

    def done(self, form_list, **kwargs):
        messages.info(self.request, 'Partner created.')
        return redirect('home')
