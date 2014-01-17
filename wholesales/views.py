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
