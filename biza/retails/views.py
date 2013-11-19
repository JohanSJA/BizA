from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

import datetime

from .models import *
from .forms import *
from stocks.models import ItemQuantity
from documents.models import Document


class SaleListView(ListView):
    def get_queryset(self):
        emp = self.request.user.employee
        if emp.hq:
            return Sale.objects.all()
        else:
            return Sale.objects.filter(store=emp.store)


class SaleCreateView(CreateView):
    form_class = SaleForm
    template_name = 'retails/sale_form.html'

    def form_valid(self, form):
        sale = form.instance
        sale.store = self.request.user.employee.store
        sale.opened_by = self.request.user
        return super(SaleCreateView, self).form_valid(form)


class SaleDetailView(DetailView):
    model = Sale

    def get_context_data(self, **kwargs):
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['lines'] = self.get_object().saleline_set.all()
        return context


class SalePrintView(SaleDetailView):
    template_name = 'retails/sale_print.html'


class SaleUpdateView(UpdateView):
    form_class = SaleForm
    template_name = 'retails/sale_form.html'

    def get_object(self, queryset=None):
        return Sale.objects.get(pk=self.kwargs['pk'])


class SaleCloseView(UpdateView):
    model = Sale
    form_class = SaleCloseForm
    template_name = 'retails/sale_close_form.html'

    def form_valid(self, form):
        sale = form.instance
        warehouse = sale.store.warehouse

        # deduct item quantities
        for line in sale.saleline_set.all():
            if line.product.is_package():
                package = line.product.package
                for pi in package.packageitem_set.all():
                    item = pi.item
                    last_quantity = item.itemquantity_set.filter(item=item, warehouse=warehouse).latest()
                    quantity_left = last_quantity.quantity - (line.quantity * pi.quantity)
                    iq = ItemQuantity(item=item, warehouse=warehouse, quantity=quantity_left, reason='S')
                    iq.save()
            else:
                item = line.product.item
                last_quantity = item.itemquantity_set.filter(item=item, warehouse=warehouse).latest()
                quantity_left = last_quantity.quantity - line.quantity
                iq = ItemQuantity(item=item, warehouse=warehouse, quantity=quantity_left, reason='S')
                iq.save()

        # set more info
        sale.closing_time = datetime.datetime.now()
        sale.closed_by = self.request.user

        # give the sale a cash bill number
        doc = Document.objects.get(name='Cash bill')
        sale.cash_bill_number = doc.get_full_name()
        doc.number += 1
        doc.save()

        return super(SaleCloseView, self).form_valid(form)


class SaleQuoteView(UpdateView):
    form_class = SaleQuoteForm
    template_name = 'retails/sale_quote_form.html'

    def get_object(self, queryset=None):
        return Sale.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        sale = form.instance

        # set more info
        sale.quoting_time = datetime.datetime.now()
        sale.quoted_by = self.request.user

        # give the sale a quotation number
        doc = Document.objects.get(name='Quotation')
        sale.quotation_number = doc.get_full_name()
        doc.number += 1
        doc.save()

        return super(SaleQuoteView, self).form_valid(form)


class SaleLineListView(ListView):
    model = SaleLine


class SaleLineCreateView(CreateView):
    form_class = SaleLineForm
    template_name = 'retails/saleline_form.html'

    def get_context_data(self, **kwargs):
        context = super(SaleLineCreateView, self).get_context_data(**kwargs)
        context['sale'] = Sale.objects.get(pk=self.kwargs['sale_pk'])
        return context

    def form_valid(self, form):
        sale = Sale.objects.get(pk=self.kwargs['sale_pk'])
        form.instance.sale = sale
        form.instance.unit_price = form.instance.product.retail_price
        return super(SaleLineCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.sale.get_absolute_url()


class SaleLineDetailView(DetailView):
    model = SaleLine


class SaleLineUpdateView(UpdateView):
    form_class = SaleLineForm
    template_name = 'retails/saleline_form.html'

    def get_object(self, queryset=None):
        return SaleLine.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(SaleLineUpdateView, self).get_context_data(**kwargs)
        context['sale'] = self.get_object().sale
        return context

    def get_success_url(self):
        return self.object.sale.get_absolute_url()


class StoreReportTemplateView(TemplateView):
    template_name = 'retails/store_report.html'

    def get_context_data(self, **kwargs):
        context = super(StoreReportTemplateView, self).get_context_data(**kwargs)
        emp = self.request.user.employee
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        context['closed_sales'] = Sale.objects.filter(closing_time__range=(today, tomorrow))
        if not emp.hq:
            context['closed_sales'] = context['closed_sales'].filter(store=emp.store)
        context['quoted_sales'] = Sale.objects.filter(quoting_time__range=(today, tomorrow), closing_time=None)
        if not emp.hq:
            context['quoted_sales'] = context['quoted_sales'].filter(store=emp.store)
        context['opened_sales'] = Sale.objects.filter(opening_time__range=(today, tomorrow), closing_time=None, quoting_time=None)
        if not emp.hq:
            context['opened_sales'] = context['opened_sales'].filter(store=emp.store)
        return context
