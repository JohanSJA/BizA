from django.conf.urls import patterns, url

from products.views import ProductLv, ProductCv, ProductDv


urlpatterns = patterns('',
    url(r'^$', ProductLv.as_view(), name='products_product_list'),
    url(r'^new/$', ProductCv.as_view(), name='products_product_new'),
    url(r'^(?P<pk>\d+)/$', ProductDv.as_view(), name='products_product_detail'),
)
