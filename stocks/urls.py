from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(r'^$', login_required(StockList.as_view()),
        name='stocks-stock-list'),
    url(r'^new/$', login_required(StockCreate.as_view()),
        name='stocks-stock-new'),
    url(r'^(?P<pk>\d+)/$', login_required(StockDetail.as_view()),
        name='stocks-stock-detail'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(StockUpdate.as_view()),
        name='stocks-stock-edit'),
    url(r'^(?P<stock_pk>\d+)/balance/$', login_required(StockBalanceList.as_view()),
        name='stocks-stock-balance-list'),
)
