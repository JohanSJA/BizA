from django.conf.urls import patterns, url

from .views import PricelistListView, PricelistPartialListView, PricelistCreateView, PricelistUpdateView


urlpatterns = patterns("",
    url(r"^pricelist/$", PricelistPartialListView.as_view(), name="products_pricelist_list"),
    url(r"^pricelist/all/$", PricelistListView.as_view(), name="products_pricelist_complete_list"),
    url(r"^pricelist/new/$", PricelistCreateView.as_view(), name="products_pricelist_create"),
    url(r"^pricelist/(?P<pk>\d+)/edit/$", PricelistUpdateView.as_view(), name="products_pricelist_update"),
)
