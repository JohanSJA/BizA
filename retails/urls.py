from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(r'^price/$', login_required(PriceList.as_view()),
        name='retails-price-list'),
    url(r'^price/new/$', login_required(PriceCreate.as_view()),
        name='retails-price-new'),
    url(r'^price/(?P<pk>\d+)/edit/$', login_required(PriceUpdate.as_view()),
        name='retails-price-edit'),

    url(r'^sale/$', login_required(SaleList.as_view()),
        name='retails-sale-list'),
    url(r'^sale/new/$', login_required(SaleCreate.as_view()),
        name='retails-sale-new'),
    url(r'^sale/(?P<pk>\d+)/$', login_required(SaleDetail.as_view()),
        name='retails-sale-detail'),
    url(r'^sale/(?P<pk>\d+)/edit/$', login_required(SaleUpdate.as_view()),
        name='retails-sale-edit'),
    url(r'^sale/(?P<pk>\d+)/close/$', login_required(SaleClose.as_view()),
        name='retails-sale-close'),
    url(r'^sale/(?P<pk>\d+)/print/$', login_required(sale_print),
        name='retails-sale-print'),
    url(r'^sale/(?P<pk>\d+)/line/edit/$', login_required(SaleLineUpdate.as_view()),
        name='retails-sale-line-edit'),
)
