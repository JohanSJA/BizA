from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from .models import *


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


class StockBalanceList(ListView):
    template_name = 'stocks/stock_balance_list.html'

    def get_queryset(self):
        return Balance.objects.filter(stock=self.kwargs['stock_pk'])

    def get_context_data(self, **kwargs):
        context = super(StockBalanceList, self).get_context_data(**kwargs)
        context['stock'] = Stock.objects.get(pk=self.kwargs['stock_pk'])
        return context
