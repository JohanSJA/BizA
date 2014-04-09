from django.conf.urls import patterns, url

from .views import (
    StockHomeView,
    UomListView, UomDetailView, UomCreateView, UomUpdateView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView,
    WarehouseListView, WarehouseDetailView, WarehouseCreateView, WarehouseUpdateView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
    ProductLogFormView
)


urlpatterns = patterns('',
    url(r"^$", StockHomeView.as_view(), name="stocks_home"),

    url(r'^uom/$', UomListView.as_view(), name='stocks_uom_list'),
    url(r'^uom/(?P<pk>\d+)/$', UomDetailView.as_view(), name='stocks_uom_detail'),
    url(r'^uom/new/$', UomCreateView.as_view(), name='stocks_uom_new'),
    url(r'^uom/(?P<pk>\d+)/edit/$', UomUpdateView.as_view(), name='stocks_uom_edit'),

    url(r'^category/$', CategoryListView.as_view(), name='stocks_category_list'),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='stocks_category_detail'),
    url(r'^category/new/$', CategoryCreateView.as_view(), name='stocks_category_new'),
    url(r'^category/(?P<pk>\d+)/edit/$', CategoryUpdateView.as_view(), name='stocks_category_edit'),

    url(r'^warehouse/$', WarehouseListView.as_view(), name='stocks_warehouse_list'),
    url(r'^warehouse/(?P<pk>\d+)/$', WarehouseDetailView.as_view(), name='stocks_warehouse_detail'),
    url(r'^warehouse/new/$', WarehouseCreateView.as_view(), name='stocks_warehouse_new'),
    url(r'^warehouse/(?P<pk>\d+)/edit/$', WarehouseUpdateView.as_view(), name='stocks_warehouse_edit'),

    url(r'^product/$', ProductListView.as_view(), name='stocks_product_list'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='stocks_product_detail'),
    url(r'^product/new/$', ProductCreateView.as_view(), name='stocks_product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='stocks_product_edit'),
    url(r'^product/(?P<pk>\d+)/log/edit/$', ProductLogFormView.as_view(), name="stocks_product_log_edit")
)
