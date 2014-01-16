from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from .models import *


class UnitList(ListView):
    model = Unit


class UnitCreate(CreateView):
    model = Unit
    success_url = reverse_lazy('stocks-unit-list')


class UnitUpdate(UpdateView):
    model = Unit
    success_url = reverse_lazy('stocks-unit-list')


class StockList(ListView):
    model = Stock


class StockCreate(CreateView):
    model = Stock
    success_url = reverse_lazy('stocks-stock-list')


class StockDetail(DetailView):
    model = Stock


class StockUpdate(UpdateView):
    model = Stock
    success_url = reverse_lazy('stocks-stock-list')


class WarehouseList(ListView):
    model = Warehouse


class WarehouseCreate(CreateView):
    model = Warehouse
    success_url = reverse_lazy('stocks-warehouse-list')


class WarehouseUpdate(UpdateView):
    model = Warehouse
    success_url = reverse_lazy('stocks-warehouse-list')


class StockBalanceList(ListView):
    template_name = 'stocks/stock_balance_list.html'

    def get_queryset(self):
        return Balance.objects.filter(stock=self.kwargs['stock_pk'])

    def get_context_data(self, **kwargs):
        context = super(StockBalanceList, self).get_context_data(**kwargs)
        context['stock'] = Stock.objects.get(pk=self.kwargs['stock_pk'])
        return context


class StockBalanceCreate(CreateView):
    template_name = 'stocks/stock_balance_form.html'
    model = Balance
