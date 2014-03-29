from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from products.models import Product
from .models import Pricelist, PricelistEntry


class PricelistListView(LoginRequiredMixin, ListView):
    model = Pricelist


class PricelistDetailView(LoginRequiredMixin, DetailView):
    model = Pricelist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pricelist = self.get_object()
        context['pricelistentry_set'] = pricelist.pricelistentry_set.all()
        return context


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'prices/product_list.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'prices/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['pricelistentry_set'] = product.pricelistentry_set.all()
        return context
