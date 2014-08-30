from django.conf.urls import patterns, url

from .views import (
    WarehouseListView, WarehouseDetailView, WarehouseCreateView, WarehouseUpdateView,
    BalanceListView, BalanceInStockListView, BalanceOutOfStockListView,
    BalanceLogListView, BalanceLogDetailView, BalanceLogCreateView, BalanceLogUpdateView,
)

urlpatterns = patterns("",
    url(r"^warehouse/$", WarehouseListView.as_view(), name="warehouse-list"),
    url(r"^warehouse/(?P<pk>\d+)/$", WarehouseDetailView.as_view(), name="warehouse-detail"),
    url(r"^warehouse/new/$", WarehouseCreateView.as_view(), name="warehouse-create"),
    url(r"^warehouse/(?P<pk>\d+)/edit/$", WarehouseUpdateView.as_view(), name="warehouse-update"),

    url(r"^balance/$", BalanceInStockListView.as_view(), name="balance-list"),
    url(r"^balance/out/$", BalanceOutOfStockListView.as_view(), name="balance-out-of-stock-list"),
    url(r"^balance/all/$", BalanceListView.as_view(), name="balance-all-list"),

    url(r"^balancelog/$", BalanceLogListView.as_view(), name="balancelog-list"),
    url(r"^balancelog/(?P<pk>\d+)/$", BalanceLogDetailView.as_view(), name="balancelog-detail"),
    url(r"^balancelog/new/$", BalanceLogCreateView.as_view(), name="balancelog-create"),
    url(r"^balancelog/(?P<pk>\d+)/edit/$", BalanceLogUpdateView.as_view(), name="balancelog-update"),
)
