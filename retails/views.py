from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from .models import *


class PriceList(ListView):
    model = Price


class PriceCreate(CreateView):
    model = Price
    success_url = reverse_lazy('retails-price-list')


class PriceUpdate(UpdateView):
    model = Price
    success_url = reverse_lazy('retails-price-list')


class SaleList(ListView):
    def get_queryset(self):
        worker_shop = self.request.user.worker.shop
        return Sale.objects.filter(shop=worker_shop)


class SaleCreate(CreateView):
    model = Sale
    fields = ['served_by']

    def form_valid(self, form):
        shop = self.request.user.worker.shop
        form.instance.shop = shop
        return super(SaleCreate, self).form_valid(form)



class SaleDetail(DetailView):
    model = Sale


class SaleUpdate(UpdateView):
    model = Sale
    fields = ['served_by']


class LineCreate(CreateView):
    model = Line
