from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(r'^stock/$', login_required(StockListView.as_view()),
        name='stocks-stock-list'),
    url(r'^stock/new/$', login_required(StockCreateView.as_view()),
        name='stocks-stock-new'),
    url(r'^stock/(?P<pk>\d+)/$', login_required(StockDetailView.as_view()),
        name='stocks-stock-detail'),
    url(r'^stock/(?P<pk>\d+)/edit/$', login_required(StockUpdateView.as_view()),
        name='stocks-stock-edit'),
    url(r'^stock/(?P<pk>\d+)/code/print/new/$',
        login_required(StockCodePrintCreateView.as_view()),
        name='stocks-stock-code-print-new'),
    url(r'^stock/(?P<pk>\d+)/code/print/start_(?P<start>\d+)_amount_(?P<amount>\d+).pdf$',
        login_required(stock_code_print_pdf),
        name='stocks-stock-code-print-pdf'),
    url(r'^stock/(?P<pk>\d+)/component/edit/$',
        login_required(StockComponentUpdateView.as_view()),
        name='stocks-stock-component-edit'),
    url(r'^warehouse/$', login_required(WarehouseListView.as_view()),
        name='stocks-warehouse-list'),
    url(r'^warehouse/new/$', login_required(WarehouseCreateView.as_view()),
        name='stocks-warehouse-new'),
    url(r'^warehouse/(?P<pk>\d+)/$',
        login_required(WarehouseDetailView.as_view()),
        name='stocks-warehouse-detail'),
    url(r'^warehouse/(?P<pk>\d+)/edit/$',
        login_required(WarehouseUpdateView.as_view()),
        name='stocks-warehouse-edit'),
    url(r'^log/$', login_required(LogListView.as_view()),
        name='stocks-log-list'),
    url(r'^log/(?P<pk>\d+)/$', login_required(LogDetailView.as_view()),
        name='stocks-log-detail'),
)
