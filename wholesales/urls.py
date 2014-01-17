from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(r'^price/$', login_required(PriceList.as_view()),
        name='wholesales-price-list'),
    url(r'^price/new/$', login_required(PriceCreate.as_view()),
        name='wholesales-price-new'),
    url(r'^price/(?P<pk>\d+)/edit/$', login_required(PriceUpdate.as_view()),
        name='wholesales-price-edit'),

    url(r'^partner/$', login_required(PartnerList.as_view()),
        name='wholesales-partner-list'),
    url(r'^partner/new/$', login_required(PartnerCreate.as_view()),
        name='wholesales-partner-new'),
    url(r'^partner/(?P<pk>\d+)/$', login_required(PartnerDetail.as_view()),
        name='wholesales-partner-detail'),
    url(r'^partner/(?P<pk>\d+)/edit/$', login_required(PartnerUpdate.as_view()),
        name='wholesales-partner-edit'),

    url(r'^sale/$', login_required(SaleList.as_view()),
        name='wholesales-sale-list'),
    url(r'^sale/new/$', login_required(SaleCreate.as_view()),
        name='wholesales-sale-new'),
    url(r'^sale/(?P<pk>\d+)/$', login_required(SaleDetail.as_view()),
        name='wholesales-sale-detail'),
    url(r'^sale/(?P<pk>\d+)/edit/$', login_required(SaleUpdate.as_view()),
        name='wholesales-sale-edit'),
    url(r'^sale/(?P<pk>\d+)/print/$', login_required(SalePrint.as_view()),
        name='wholesales-sale-print'),
    url(r'^saleline/new/$', login_required(SaleLineCreate.as_view()),
        name='wholesales-saleline-new'),

    url(r'^purchase/$', login_required(PurchaseList.as_view()),
        name='wholesales-purchase-list'),
    url(r'^purchase/new/$', login_required(PurchaseCreate.as_view()),
        name='wholesales-purchase-new'),
    url(r'^purchase/(?P<pk>\d+)/$', login_required(PurchaseDetail.as_view()),
        name='wholesales-purchase-detail'),
    url(r'^purchase/(?P<pk>\d+)/edit/$', login_required(PurchaseUpdate.as_view()),
        name='wholesales-purchase-edit'),
    url(r'^purchaseline/new/$', login_required(PurchaseLineCreate.as_view()),
        name='wholesales-purchaseline-new'),
)
