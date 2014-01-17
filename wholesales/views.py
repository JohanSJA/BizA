from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from datetime import datetime

from .models import *


class PriceList(ListView):
    model = Price


class PriceCreate(CreateView):
    model = Price
    success_url = reverse_lazy('retails-price-list')


class PriceUpdate(UpdateView):
    model = Price
    success_url = reverse_lazy('retails-price-list')


class PartnerList(ListView):
    model = Partner


class PartnerCreate(CreateView):
    model = Partner


class PartnerDetail(DetailView):
    model = Partner


class PartnerUpdate(UpdateView):
    model = Partner


class SaleList(ListView):
    model = Sale


class SaleCreate(CreateView):
    model = Sale
    fields = ['partner', 'served_by']


class SaleDetail(DetailView):
    model = Sale


class SaleUpdate(UpdateView):
    model = Sale
    fields = ['partner', 'served_by']


class SalePrint(DetailView):
    model = Sale
    template_name = 'wholesales/sale_print.html'


class SaleLineCreate(CreateView):
    model = SaleLine


class PurchaseList(ListView):
    model = Purchase


class PurchaseCreate(CreateView):
    model = Purchase


class PurchaseDetail(DetailView):
    model = Purchase


class PurchaseUpdate(UpdateView):
    model = Purchase


class PurchaseLineCreate(CreateView):
    model = PurchaseLine
