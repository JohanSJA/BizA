from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('stocks.views',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^biza/', include('biza.foo.urls')),
    url(r'^product/$', login_required(ProductListView.as_view()), name='stocks_product_list'),
    url(r'^product/(?P<pk>\d+)/$', login_required(ProductDetailView.as_view()), name='stocks_product_detail'),
    url(r'^product/(?P<pk>\d+)_barcode.svg$', login_required(product_barcode_svg), name='stocks_product_barcode'),
    url(r'^product/(?P<pk>\d+)/printing/$', login_required(ProductPrintingView.as_view()), name='stocks_product_printing'),
    url(r'^product/(?P<pk>\d+)/printing/pdf/$', login_required(product_printing_pdf_view), name='stocks_product_printing_pdf'),
    url(r'^item/new/$', login_required(ItemCreateView.as_view()), name='stocks_item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', login_required(ItemUpdateView.as_view()), name='stocks_item_edit'),
    url(r'^product/(?P<item_pk>\d+)/itemquantity/new/$', login_required(ItemQuantityCreateView.as_view()), name='stocks_itemquantity_new'),
    url(r'^product/(?P<item_pk>\d+)/itemquantitystore/new/$', login_required(ItemQuantityStoreCreateView.as_view()), name='stocks_itemquantitystore_new'),
    url(r'^package/new/$', login_required(PackageCreateView.as_view()), name='stocks_package_new'),
    url(r'^package/(?P<pk>\d+)/edit/$', login_required(PackageUpdateView.as_view()), name='stocks_package_edit'),
    url(r'^package/(?P<pk>\d+)/edit_price/$', login_required(PackagePriceUpdateView.as_view()), name='stocks_package_edit_price'),
    url(r'^product/(?P<package_pk>\d+)/packageitem/new/$', login_required(PackageItemCreateView.as_view()), name='stocks_packageitem_new'),
    url(r'^packageitem/(?P<pk>\d+)/edit/$', login_required(PackageItemUpdateView.as_view()), name='stocks_packageitem_edit'),
)
