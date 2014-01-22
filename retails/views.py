from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy, reverse

from datetime import datetime

from .models import *
from .forms import *


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
        user = self.request.user
        shop = user.worker.shop
        form.instance.shop = shop
        return super(SaleCreate, self).form_valid(form)



class SaleDetail(DetailView):
    model = Sale


class SaleUpdate(UpdateView):
    model = Sale
    fields = ['served_by']


class SaleClose(UpdateView):
    model = Sale
    form_class = SaleCloseForm
    template_name = 'retails/sale_close_form.html'

    def form_valid(self, form):
        sale = form.instance
        sale.closed_by = self.request.user
        sale.closed_at = datetime.now()
        form.instance = sale
        return super(SaleClose, self).form_valid(form)


class SalePrint(DetailView):
    model = Sale
    template_name = 'retails/sale_print.html'


class SaleLineUpdate(UpdateView):
    model = Sale
    form_class = SaleLineFormSet
    template_name = 'retails/sale_line_form.html'

    def get_success_url(self):
        return reverse('retails-sale-detail', args=[self.kwargs['pk']])
