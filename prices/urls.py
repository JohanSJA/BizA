from django.conf.urls import patterns, url

from .views import (
    PricelistListView, PricelistDetailView,
    ProductListView, ProductDetailView
)


urlpatterns = patterns('',
    url(r'^pricelist/$', PricelistListView.as_view(), name='prices_pricelist_list'),
    url(r'^pricelist/(?P<pk>\d+)/$', PricelistDetailView.as_view(), name='prices_pricelist_detail'),

    url(r'^product/$', ProductListView.as_view(), name='prices_product_list'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='prices_product_detail')
)
