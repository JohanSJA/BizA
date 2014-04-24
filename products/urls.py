from django.conf.urls import patterns, url

from .views import (
    ProductHomeView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView
)


urlpatterns = patterns('',
    url(r"^$", ProductHomeView.as_view(), name="products_home"),

    url(r"^category/$", CategoryListView.as_view(), name="products_category_list"),
    url(r"^category/(?P<pk>\d+)/$", CategoryDetailView.as_view(), name="products_category_detail"),
    url(r"^category/new/$", CategoryCreateView.as_view(), name="products_category_create"),
    url(r"^category/(?P<pk>\d+)/edit/$", CategoryUpdateView.as_view(), name="products_category_update"),
)
