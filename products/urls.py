from django.conf.urls import patterns, url

from .views import (
    ProductHomeView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView,
    UomListView, UomDetailView, UomCreateView, UomUpdateView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
    PricelistListView, PricelistPartialListView, PricelistCreateView, PricelistUpdateView,
    WarehouseListView, WarehouseDetailView, WarehouseCreateView, WarehouseUpdateView,
    BalanceListView, BalanceInStockListView, BalanceOutOfStockListView,
    BalanceLogListView, BalanceLogDetailView, BalanceLogCreateView, BalanceLogUpdateView,
)


urlpatterns = patterns('',
    url(r"^$", ProductHomeView.as_view(), name="products_home"),

    url(r"^category/$", CategoryListView.as_view(), name="products_category_list"),
    url(r"^category/(?P<pk>\d+)/$", CategoryDetailView.as_view(), name="products_category_detail"),
    url(r"^category/new/$", CategoryCreateView.as_view(), name="products_category_create"),
    url(r"^category/(?P<pk>\d+)/edit/$", CategoryUpdateView.as_view(), name="products_category_update"),

#    url(r"^uom/$", UomListView.as_view(), name="products_uom_list"),
#    url(r"^uom/(?P<pk>\d+)/$", UomDetailView.as_view(), name="products_uom_detail"),
#    url(r"^uom/new/$", UomCreateView.as_view(), name="products_uom_create"),
#    url(r"^uom/(?P<pk>\d+)/edit/$", UomUpdateView.as_view(), name="products_uom_update"),

    url(r"^product/$", ProductListView.as_view(), name="products_product_list"),
    url(r"^product/(?P<pk>\d+)/$", ProductDetailView.as_view(), name="products_product_detail"),
    url(r"^product/new/$", ProductCreateView.as_view(), name="products_product_create"),
    url(r"^product/(?P<pk>\d+)/edit/$", ProductUpdateView.as_view(), name="products_product_update"),

    url(r"^pricelist/$", PricelistPartialListView.as_view(), name="products_pricelist_list"),
    url(r"^pricelist/all/$", PricelistListView.as_view(), name="products_pricelist_complete_list"),
    url(r"^pricelist/new/$", PricelistCreateView.as_view(), name="products_pricelist_create"),
    url(r"^pricelist/(?P<pk>\d+)/edit/$", PricelistUpdateView.as_view(), name="products_pricelist_update"),

    url(r"^warehouse/$", WarehouseListView.as_view(), name="products_warehouse_list"),
    url(r"^warehouse/(?P<pk>\d+)/$", WarehouseDetailView.as_view(), name="products_warehouse_detail"),
    url(r"^warehouse/new/$", WarehouseCreateView.as_view(), name="products_warehouse_create"),
    url(r"^warehouse/(?P<pk>\d+)/edit/$", WarehouseUpdateView.as_view(), name="products_warehouse_update"),

    url(r"^balance/$", BalanceInStockListView.as_view(), name="products_balance_list"),
    url(r"^balance/out/$", BalanceOutOfStockListView.as_view(), name="products_balance_out_of_stock_list"),
    url(r"^balance/all/$", BalanceListView.as_view(), name="products_balance_all_list"),

    url(r"^balancelog/$", BalanceLogListView.as_view(), name="products_balancelog_list"),
    url(r"^balancelog/(?P<pk>\d+)/$", BalanceLogDetailView.as_view(), name="products_balancelog_detail"),
    url(r"^balancelog/new/$", BalanceLogCreateView.as_view(), name="products_balancelog_create"),
    url(r"^balancelog/(?P<pk>\d+)/edit/$", BalanceLogUpdateView.as_view(), name="products_balancelog_update"),
)
