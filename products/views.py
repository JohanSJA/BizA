from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet, SearchableListMixin

from .models import (
    Category, Uom, Product, Pricelist, PricelistEntry, Warehouse,
    BalanceLog, BalanceLogEntry
)
from .forms import PricelistForm


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


class ProductListView(SearchableListMixin, ListView):
    model = Product
    paginate_by = 50
    search_fields = ["model", "description"]

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["pricelistentry_list"] = product.pricelistentry_set.all()
        return context

class ProductCreateView(CreateWithInlinesView):
    model = Product
    inlines = [PricelistEntryInlineFormSet]

class ProductUpdateView(UpdateWithInlinesView):
    model = Product
    inlines = [PricelistEntryInlineFormSet]


class PricelistListView(SearchableListMixin, ListView):
    model = Product
    template_name = "products/pricelist_list.html"
    paginate_by = 50
    search_fields = ["model", "description"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _, _, product_list, _ = self.paginate_queryset(self.get_queryset(), self.paginate_by)
        pricelist_list = Pricelist.objects.all()
        for product in product_list:
            product.prices = []
            for pricelist in pricelist_list:
                price = [None, None]
                try:
                    price_entry = PricelistEntry.objects.get(pricelist=pricelist, product=product)
                    price = [price_entry.price, "actual"]
                except ObjectDoesNotExist:
                    if pricelist.base:
                        try:
                            price_entry = PricelistEntry.objects.get(pricelist=pricelist.base, product=product)
                            price = price_entry.price * pricelist.base_derivation / 100
                            price = [price, "derived"]
                        except ObjectDoesNotExist:
                            pass
                product.prices.append(price)
        context["product_list"] = product_list
        context["pricelist_list"] = pricelist_list
        return context

class PricelistPartialListView(PricelistListView):
    def get_queryset(self):
        products = super().get_queryset()
        pricelist_entries = PricelistEntry.objects.all().values("product")
        products = products.filter(pk__in=pricelist_entries)
        return products

class PricelistCreateView(CreateWithInlinesView):
    model = Pricelist
    form_class = PricelistForm
    success_url = reverse_lazy("products_pricelist_list")

class PricelistUpdateView(UpdateWithInlinesView):
    model = Pricelist
    form_class = PricelistForm
    success_url = reverse_lazy("products_pricelist_list")


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
