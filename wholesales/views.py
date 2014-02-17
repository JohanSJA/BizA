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


class SaleDetail(DetailView):
    model = Sale


class SaleUpdate(UpdateView):
    model = Sale


class SalePlaceOrder(UpdateView):
    model = Sale
    form_class = SalePlaceOrderForm
    template_name = 'wholesales/sale_place_order.html'

    def get_success_url(self):
        return reverse_lazy('wholesales-sale-detail', args=[self.kwargs['pk']])


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


class PurchaseDetail(DetailView):
    model = Purchase


class PurchaseUpdate(UpdateView):
    model = Purchase


class PurchasePurchaseLineUpdate(UpdateView):
    model = Purchase
    form_class = PurchasePurchaseLineFormSet
    template_name = 'wholesales/purchase_purchaseline_form.html'

    def get_success_url(self):
        return reverse_lazy('wholesales-purchase-detail', args=[self.kwargs['pk']])


class PurchasePlaceOrder(UpdateView):
    model = Purchase
    form_class = PurchasePlaceOrderForm
    template_name = 'wholesales/purchase_place_order.html'

    def form_valid(self, form):
        purchase = form.instance

        po = PurchaseOrder(purchase=purchase)
        po.save()

        return super().form_valid(form)


class PurchaseInvoiceCreate(CreateView):
    model = PurchaseInvoice
    form_class = PurchaseInvoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchase = Purchase.objects.get(pk=self.kwargs['pk'])
        context['purchase'] = purchase
        return context

    def form_valid(self, form):
        invoice = form.instance

        purchase = Purchase.objects.get(pk=self.kwargs['pk'])
        invoice.purchase = purchase

        warehouse = form.cleaned_data['warehouse']

        for line in purchase.purchaseline_set.all():
            log = Log.objects.get(
                    warehouse=warehouse,
                    stock=line.stock)
            new_entry = Entry(log=log, changes=line.quantity, reason='WP')
            new_entry.save()

        form.instance = invoice
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wholesales-purchase-detail', args=[self.kwargs['pk']])
