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
    def get_queryset(self):
        product_list = Product.objects.all()
        if self.request.GET:
            if "search" in self.request.GET:
                product_list = product_list.filter(model__icontains=self.request.GET["search"])
        return product_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            if "search" in self.request.GET:
                context["search_term"] = self.request.GET["search"]
        return context

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["pricelistentry_list"] = product.pricelistentry_set.all()
        return context

class ProductCreateView(CreateWithInlinesView):
    model = Product
    inlines = [PricelistEntryInlineFormSet,]

class ProductUpdateView(UpdateWithInlinesView):
    model = Product
    inlines = [PricelistEntryInlineFormSet,]


class PricelistListView(ListView):
    model = Pricelist

class PricelistDetailView(DetailView):
    model = Pricelist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pricelist = self.get_object()
        context["pricelistentry_list"] = pricelist.pricelistentry_set.all()
        return context

class PricelistCreateView(CreateWithInlinesView):
    model = Pricelist
    inlines = [PricelistEntryInlineFormSet,]

class PricelistUpdateView(UpdateWithInlinesView):
    model = Pricelist
    inlines = [PricelistEntryInlineFormSet,]


class WarehouseListView(ListView):
    model = Warehouse

class WarehouseDetailView(DetailView):
    model = Warehouse

class WarehouseCreateView(CreateView):
    model = Warehouse

class WarehouseUpdateView(UpdateView):
    model = Warehouse


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
