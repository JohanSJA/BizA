from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('stocks.views',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^biza/', include('biza.foo.urls')),
    url(r'^product/$', login_required(ProductListView.as_view()), name='stocks_product_list'),
    url(r'^product/(?P<pk>\d+)/$', login_required(ProductDetailView.as_view()), name='stocks_product_detail'),
    url(r'^item/new/$', login_required(ItemCreateView.as_view()), name='stocks_item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', login_required(ItemUpdateView.as_view()), name='stocks_item_edit'),
)
