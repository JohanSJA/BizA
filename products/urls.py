from django.conf.urls import patterns, url

from .views import (
    ProductHomeView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView,
    UomListView, UomDetailView, UomCreateView, UomUpdateView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
    PricelistListView, PricelistDetailView, PricelistCreateView, PricelistUpdateView,
)


urlpatterns = patterns('',
    url(r"^$", ProductHomeView.as_view(), name="products_home"),

    url(r"^category/$", CategoryListView.as_view(), name="products_category_list"),
    url(r"^category/(?P<pk>\d+)/$", CategoryDetailView.as_view(), name="products_category_detail"),
    url(r"^category/new/$", CategoryCreateView.as_view(), name="products_category_create"),
    url(r"^category/(?P<pk>\d+)/edit/$", CategoryUpdateView.as_view(), name="products_category_update"),

    url(r"^uom/$", UomListView.as_view(), name="products_uom_list"),
    url(r"^uom/(?P<pk>\d+)/$", UomDetailView.as_view(), name="products_uom_detail"),
    url(r"^uom/new/$", UomCreateView.as_view(), name="products_uom_create"),
    url(r"^uom/(?P<pk>\d+)/edit/$", UomUpdateView.as_view(), name="products_uom_update"),

    url(r"^product/$", ProductListView.as_view(), name="products_product_list"),
    url(r"^product/(?P<pk>\d+)/$", ProductDetailView.as_view(), name="products_product_detail"),
    url(r"^product/new/$", ProductCreateView.as_view(), name="products_product_create"),
    url(r"^product/(?P<pk>\d+)/edit/$", ProductUpdateView.as_view(), name="products_product_update"),

    url(r"^pricelist/$", PricelistListView.as_view(), name="products_pricelist_list"),
    url(r"^pricelist/(?P<pk>\d+)/$", PricelistDetailView.as_view(), name="products_pricelist_detail"),
    url(r"^pricelist/new/$", PricelistCreateView.as_view(), name="products_pricelist_create"),
    url(r"^pricelist/(?P<pk>\d+)/edit/$", PricelistUpdateView.as_view(), name="products_pricelist_update"),
)
