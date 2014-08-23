from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet, SearchableListMixin

from products.models import Product

from .forms import PricelistForm
from .models import Pricelist, PricelistEntry


class PricelistEntryInlineFormSet(InlineFormSet):
    model = PricelistEntry


class PricelistListView(SearchableListMixin, ListView):
    model = Product
    template_name = "prices/pricelist_list.html"
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
