from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet

from .models import (
    Category, Uom, Product, Pricelist, PricelistEntry, Warehouse,
    BalanceLog, BalanceLogEntry
)


class ProductHomeView(TemplateView):
    template_name = "products/home.html"


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["product_list"] = category.product_set.all()
        return context

class CategoryCreateView(CreateView):
    model = Category

class CategoryUpdateView(UpdateView):
    model = Category


class UomListView(ListView):
    model = Uom

class UomDetailView(DetailView):
    model = Uom

class UomCreateView(CreateView):
    model = Uom
    template_name = "base_form.html"

class UomUpdateView(UpdateView):
    model = Uom
    template_name = "base_form.html"


class PricelistEntryInlineFormSet(InlineFormSet):
    model = PricelistEntry


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product


class PricelistListView(ListView):
    model = Pricelist
    template_name = "base_list.html"

class PricelistDetailView(DetailView):
    model = Pricelist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pricelist = self.get_object()
        context["pricelistentry_list"] = pricelist.pricelistentry_set.all()
        return context

class PricelistCreateView(CreateWithInlinesView):
    model = Pricelist
    inlines = [PricelistEntryInlineFormSet]
    template_name = "base_form_with_inlines.html"

class PricelistUpdateView(UpdateWithInlinesView):
    model = Pricelist
    inlines = [PricelistEntryInlineFormSet]
    template_name = "base_form_with_inlines.html"


class WarehouseListView(ListView):
    model = Warehouse

class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "base_detail.html"

class WarehouseCreateView(CreateView):
    model = Warehouse
    template_name = "base_form.html"

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    template_name = "base_form.html"


class BalanceLogListView(ListView):
    model = BalanceLog

class BalanceLogDetailView(DetailView):
    model = BalanceLog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        balancelog = self.get_object()
        context["balancelogentry_list"] = balancelog.balancelogentry_set.all()
        return context

class BalanceLogCreateView(CreateView):
    model = BalanceLog
    template_name = "base_form.html"

class BalanceLogUpdateView(UpdateView):
    model = BalanceLog
    template_name = "base_form.html"
