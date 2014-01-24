from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from datetime import datetime

from .models import *
from .forms import *


class PriceList(ListView):
    model = Price


class PriceCreate(CreateView):
    model = Price
    success_url = reverse_lazy('wholesales-price-list')


class PriceUpdate(UpdateView):
    model = Price
    success_url = reverse_lazy('wholesales-price-list')


class PartnerList(ListView):
    model = Partner


class PartnerCreate(CreateView):
    model = Partner


class PartnerDetail(DetailView):
    model = Partner


class PartnerUpdate(UpdateView):
    model = Partner


class PartnerLocationUpdate(UpdateView):
    model = Partner
    form_class = PartnerLocationFormSet
    template_name = 'wholesales/partner_location_formset.html'

    def get_success_url(self):
        return reverse_lazy('wholesales-partner-detail', kwargs={'pk': self.kwargs['pk']})


class SaleList(ListView):
    model = Sale


class SaleCreate(CreateView):
    model = Sale
    fields = ['partner', 'served_by', 'term']


class SaleDetail(DetailView):
    model = Sale


class SaleUpdate(UpdateView):
    model = Sale
    fields = ['partner', 'served_by', 'term']


class SaleClose(UpdateView):
    model = Sale
    fields = ['closed']


class SalePrint(DetailView):
    model = Sale
    template_name = 'wholesales/sale_print.html'


class SaleSaleLineUpdate(UpdateView):
    model = Sale
    form_class = SaleSaleLineFormSet
    template_name = 'wholesales/sale_saleline_form.html'

    def get_success_url(self):
        return reverse_lazy('wholesales-sale-detail', args=[self.kwargs['pk']])


class PurchaseList(ListView):
    model = Purchase


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['partner', 'doc_num', 'date']


class PurchaseDetail(DetailView):
    model = Purchase


class PurchaseUpdate(UpdateView):
    model = Purchase
    fields = ['partner', 'doc_num', 'date']


class PurchaseClose(UpdateView):
    model = Purchase
    fields = ['closed']


class PurchasePurchaseLineUpdate(UpdateView):
    model = Purchase
    form_class = PurchasePurchaseLineFormSet
    template_name = 'wholesales/purchase_purchaseline_form.html'

    def get_success_url(self):
        return reverse_lazy('wholesales-purchase-detail', args=[self.kwargs['pk']])
