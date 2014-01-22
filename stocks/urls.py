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
    url(r'^(?P<pk>\d+)/code/print/new/$', login_required(StockCodePrintCreate.as_view()),
        name='stocks-stock-code-print-new'),
    url(r'^(?P<pk>\d+)/code/print/start_(?P<start>\d+)_amount_(?P<amount>\d+).pdf$',
        login_required(stock_code_print_pdf), name='stocks-stock-code-print-pdf'),
    url(r'^(?P<stock_pk>\d+)/balance/$', login_required(StockBalanceList.as_view()),
        name='stocks-stock-balance-list'),
)
