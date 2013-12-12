from django.conf.urls import patterns, url

from products.views import ProductLv, ProductDv


urlpatterns = patterns('',
    url(r'^$', ProductLv.as_view(), name='products_product_list'),
    url(r'^(?P<pk>\d+)/$', ProductDv.as_view(), name='products_product_detail'),
)
