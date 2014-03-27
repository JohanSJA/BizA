from django.conf.urls import patterns, url

from .views import (
    UomListView, UomDetailView, UomCreateView, UomUpdateView,
    WarehouseListView, WarehouseDetailView, WarehouseCreateView, WarehouseUpdateView,
    StockListView, StockDetailView, StockCreateView, StockUpdateView,
)


urlpatterns = patterns('',
    url(r'^uom/$', UomListView.as_view(), name='stocks_uom_list'),
    url(r'^uom/(?P<pk>\d+)/$', UomDetailView.as_view(), name='stocks_uom_detail'),
    url(r'^uom/new/$', UomCreateView.as_view(), name='stocks_uom_new'),
    url(r'^uom/(?P<pk>\d+)/edit/$', UomUpdateView.as_view(), name='stocks_uom_edit'),

    url(r'^warehouse/$', WarehouseListView.as_view(), name='stocks_warehouse_list'),
    url(r'^warehouse/(?P<pk>\d+)/$', WarehouseDetailView.as_view(), name='stocks_warehouse_detail'),
    url(r'^warehouse/new/$', WarehouseCreateView.as_view(), name='stocks_warehouse_new'),
    url(r'^warehouse/(?P<pk>\d+)/edit/$', WarehouseUpdateView.as_view(), name='stocks_warehouse_edit'),

    url(r'^stock/$', StockListView.as_view(), name='stocks_stock_list'),
    url(r'^stock/(?P<pk>\d+)/$', StockDetailView.as_view(), name='stocks_stock_detail'),
    url(r'^stock/new/$', StockCreateView.as_view(), name='stocks_stock_new'),
    url(r'^stock/(?P<pk>\d+)/edit/$', StockUpdateView.as_view(), name='stocks_stock_edit'),
)
