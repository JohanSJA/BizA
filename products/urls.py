from django.conf.urls import patterns, url

from .views import (
    UomListView, UomCreateView, UomUpdateView,
    ProductListView, ProductCreateView, ProductUpdateView,
)


urlpatterns = patterns('',
    url(r'^uom/$', UomListView.as_view(), name='products_uom_list'),
    url(r'^uom/new/$', UomCreateView.as_view(), name='products_uom_new'),
    url(r'^uom/(?P<pk>\d+)/edit/$', UomUpdateView.as_view(), name='products_uom_edit'),

    url(r'^product/$', ProductListView.as_view(), name='products_product_list'),
    url(r'^product/new/$', ProductCreateView.as_view(), name='products_product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='products_product_edit'),
)
