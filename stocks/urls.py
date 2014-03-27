from django.conf.urls import patterns, url

from .views import (
    UomListView, UomDetailView, UomCreateView, UomUpdateView,
    WarehouseListView, WarehouseDetailView, WarehouseCreateView, WarehouseUpdateView,
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
)
