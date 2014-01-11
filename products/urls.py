from django.conf.urls import patterns, url

from products.views import *

urlpatterns = patterns('',
    url(r'^$', ProductTv.as_view(), name='products_home'),
    url(r'^product/$', ProductLv.as_view(), name='products_product_list'),
    url(r'^product/new/$', ProductCv.as_view(), name='products_product_new'),
    url(r'^product/(?P<pk>\d+)/$', ProductDv.as_view(), name='products_product_detail'),
    url(r'^product/(?P<pk>\d+)/edit/$', ProductUv.as_view(), name='products_product_edit'),
    url(
        r'^product/(?P<product_pk>\d+)/component/new/$',
        ComponentCv.as_view(),
        name='products_component_new'
    ),
    url(
        r'^product/(?P<product_pk>\d+)/quantity/new/$',
        QuantityCreateView.as_view(),
        name='products_quantity_new'
    ),
)
