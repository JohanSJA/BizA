from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

import datetime

from .models import *
from .forms import *
from stocks.models import ItemQuantity


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
        form.instance.store = self.request.user.employee.store
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
    form_class = SaleCloseForm
    template_name = 'retails/sale_close_form.html'

    def get_object(self, queryset=None):
        return Sale.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        sale = form.instance
        warehouse = sale.store.warehouse
        for line in sale.saleline_set.all():
            if line.product.is_package():
                package = line.product.package
                for pi in package.packageitem_set.all():
                    item = pi.item
                    last_quantity = item.itemquantity_set.filter(item=item, warehouse=warehouse).latest()
                    quantity_left = last_quantity.quantity - (line.quantity * pi.quantity)
                    iq = ItemQuantity(item=item, warehouse=warehouse, quantity=quantity_left)
                    iq.save()
            else:
                item = line.product.item
                last_quantity = item.itemquantity_set.filter(item=item, warehouse=warehouse).latest()
                quantity_left = last_quantity.quantity - line.quantity
                iq = ItemQuantity(item=item, warehouse=warehouse, quantity=quantity_left)
                iq.save()
        sale.closing_time = datetime.datetime.now()
        return super(SaleCloseView, self).form_valid(form)

class SaleLineListView(ListView):
    model = SaleLine


class SaleLineCreateView(CreateView):
    model = SaleLine

    def get_success_url(self):
        return self.object.sale.get_absolute_url()


class SaleLineDetailView(DetailView):
    model = SaleLine


class SaleLineUpdateView(UpdateView):
    model = SaleLine

    def get_success_url(self):
        return self.object.sale.get_absolute_url()
