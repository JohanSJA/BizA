from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(r'^stock/$', login_required(StockList.as_view()),
        name='stocks-stock-list'),
    url(r'^stock/new/$', login_required(StockCreate.as_view()),
        name='stocks-stock-new'),
    url(r'^stock/(?P<pk>\d+)/$', login_required(StockDetail.as_view()),
        name='stocks-stock-detail'),
    url(r'^stock/(?P<pk>\d+)/edit/$', login_required(StockUpdate.as_view()),
        name='stocks-stock-edit'),
    url(r'^stock/(?P<pk>\d+)/code/print/new/$', login_required(StockCodePrintCreate.as_view()),
        name='stocks-stock-code-print-new'),
    url(r'^stock/(?P<pk>\d+)/code/print/start_(?P<start>\d+)_amount_(?P<amount>\d+).pdf$',
        login_required(stock_code_print_pdf), name='stocks-stock-code-print-pdf'),
    url(r'^stock/(?P<pk>\d+)/component/edit/$', login_required(StockComponentUpdate.as_view()),
        name='stocks-stock-component-edit'),
    url(r'^stock/(?P<stock_pk>\d+)/balance/$', login_required(StockBalanceList.as_view()),
        name='stocks-stock-balance-list'),
    url(r'^warehouse/$', login_required(WarehouseList.as_view()),
        name='stocks-warehouse-list'),
    url(r'^warehouse/new/$', login_required(WarehouseCreate.as_view()),
        name='stocks-warehouse-new'),
    url(r'^warehouse/(?P<pk>\d+)/$', login_required(WarehouseDetail.as_view()),
        name='stocks-warehouse-detail'),
    url(r'^warehouse/(?P<pk>\d+)/edit/$', login_required(WarehouseUpdate.as_view()),
        name='stocks-warehouse-edit'),
    url(r'^log/$', login_required(LogList.as_view()), name='stocks-log-list'),
    url(r'^log/new/$', login_required(LogCreate.as_view()),
        name='stocks-log-new'),
    url(r'^log/(?P<pk>\d+)/$', login_required(LogDetail.as_view()),
        name='stocks-log-detail'),
)
