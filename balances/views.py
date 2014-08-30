from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from extra_views import CreateWithInlinesView, InlineFormSet, SearchableListMixin

from products.models import Product

from .models import Warehouse, BalanceLog, BalanceLogEntry


class WarehouseListView(ListView):
    model = Warehouse

class WarehouseDetailView(DetailView):
    model = Warehouse

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        warehouse = self.get_object()
        context["balancelog_list"] = warehouse.balancelog_set.all()
        return context

class WarehouseCreateView(CreateView):
    model = Warehouse

class WarehouseUpdateView(UpdateView):
    model = Warehouse


class BalanceListView(SearchableListMixin, ListView):
    model = Product
    template_name = "products/balance_list.html"
    paginate_by = 50
    search_fields = ["model", "description"]


class BalanceInStockListView(BalanceListView):
    def get_queryset(self):
        product_list = super().get_queryset().all()
        new_product_list = []
        for product in product_list:
            if product.balance() > 0:
                new_product_list.append(product)
        return new_product_list


class BalanceOutOfStockListView(BalanceListView):
    def get_queryset(self):
        product_list = super().get_queryset().all()
        new_product_list = []
        for product in product_list:
            if product.balance() <= 0:
                new_product_list.append(product)
        return new_product_list


class BalanceLogEntryInlineFormSet(InlineFormSet):
    model = BalanceLogEntry


class BalanceLogListView(ListView):
    model = BalanceLog

class BalanceLogDetailView(DetailView):
    model = BalanceLog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        balancelog = self.get_object()
        context["balancelogentry_list"] = balancelog.balancelogentry_set.all()
        return context

class BalanceLogCreateView(CreateWithInlinesView):
    model = BalanceLog
    inlines = [BalanceLogEntryInlineFormSet]
    template_name = "products/balancelog_form_with_inlines.html"

class BalanceLogUpdateView(UpdateView):
    model = BalanceLog
