from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from datetime import datetime

from stocks.models import Log, Entry

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
        sale = form.instance

        sale.shop = shop

        return super().form_valid(form)



class SaleDetail(DetailView):
    model = Sale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sale = self.get_object()
        if not sale.closed():
            for line in sale.line_set.all():
                log = Log.objects.filter(
                        warehouse=sale.shop.warehouse,
                        stock=line.stock).first()
                if log:
                    if log.balance() < line.quantity:
                        messages.warning(self.request, 'Not enough {} for sale.'.format(line.stock))
                else:
                    messages.warning(self.request, 'Not {} in warehouse.'.format(line.stock))

        return context


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

        receipt = Receipt(sale=sale)
        receipt.save()

        for line in sale.line_set.all():
            log = Log.objects.get(
                    warehouse=sale.shop.warehouse,
                    stock=line.stock)
            new_entry = Entry(log=log, changes=-(line.quantity), reason='RS')
            new_entry.save()

        return super().form_valid(form)


class SalePrint(DetailView):
    model = Sale
    template_name = 'retails/sale_print.html'


class SaleLineUpdate(UpdateView):
    model = Sale
    form_class = SaleLineFormSet
    template_name = 'retails/sale_line_formset.html'

    def get_success_url(self):
        return reverse_lazy('retails-sale-detail', args=[self.kwargs['pk']])
