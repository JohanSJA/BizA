from django.conf.urls import patterns, url

from products.views import (
        ProductLv, ProductCv, ProductDv, ProductUv,
        ComponentCv, QuantityCreateView
        )


urlpatterns = patterns('',
    url(r'^$', ProductLv.as_view(), name='products_product_list'),
    url(r'^new/$', ProductCv.as_view(), name='products_product_new'),
    url(r'^(?P<pk>\d+)/$', ProductDv.as_view(), name='products_product_detail'),
    url(r'^(?P<pk>\d+)/edit/$', ProductUv.as_view(), name='products_product_edit'),
    url(
        r'^(?P<product_pk>\d+)/component/new/$',
        ComponentCv.as_view(),
        name='products_component_new'
    ),
    url(
        r'^(?P<product_pk>\d+)/quantity/new/$',
        QuantityCreateView.as_view(),
        name='products_quantity_new'
    ),
)
