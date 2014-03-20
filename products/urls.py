from django.conf.urls import patterns, url

from .views import (
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
)


urlpatterns = patterns('',
    url(r'^category/$', CategoryListView.as_view(), name='products_category_list'),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='products_category_detail'),
    url(r'^category/new/$', CategoryCreateView.as_view(), name='products_category_new'),
    url(r'^category/(?P<pk>\d+)/edit/$', CategoryUpdateView.as_view(), name='products_category_edit'),

    url(r'^product/$', ProductListView.as_view(), name='products_product_list'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='products_product_detail'),
    url(r'^product/new/$', ProductCreateView.as_view(), name='products_product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='products_product_edit'),
)
