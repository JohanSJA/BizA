from django.conf.urls import patterns, url

from .views import (
    UomListView, UomDetailView, UomCreateView, UomUpdateView,
)


urlpatterns = patterns('',
    url(r'^uom/$', UomListView.as_view(), name='stocks_uom_list'),
    url(r'^uom/(?P<pk>\d+)/$', UomDetailView.as_view(), name='stocks_uom_detail'),
    url(r'^uom/new/$', UomCreateView.as_view(), name='stocks_uom_new'),
    url(r'^uom/(?P<pk>\d+)/edit/$', UomUpdateView.as_view(), name='stocks_uom_edit'),
)
