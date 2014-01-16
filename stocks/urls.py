from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^unit/$', login_required(UnitList.as_view()),
        name='stocks-unit-list'),
    url(r'^unit/new/$', login_required(UnitCreate.as_view()),
        name='stocks-unit-new'),
    url(r'^unit/(?P<pk>\d+)/edit/$', login_required(UnitUpdate.as_view()),
        name='stocks-unit-edit'),
    url(r'^stock/$', login_required(StockList.as_view()),
        name='stocks-stock-list'),
    url(r'^stock/new/$', login_required(StockCreate.as_view()),
        name='stocks-stock-new'),
    url(r'^stock/(?P<pk>\d+)/$', login_required(StockDetail.as_view()),
        name='stocks-stock-detail'),
    url(r'^stock/(?P<pk>\d+)/edit/$', login_required(StockUpdate.as_view()),
        name='stocks-stock-edit'),
    url(r'^warehouse/$', login_required(WarehouseList.as_view()),
        name='stocks-warehouse-list'),
    url(r'^warehouse/new/$', login_required(WarehouseCreate.as_view()),
        name='stocks-warehouse-new'),
    url(r'^warehouse/(?P<pk>\d+)/edit/$', login_required(WarehouseUpdate.as_view()),
        name='stocks-warehouse-edit'),
    url(r'^stock/(?P<stock_pk>\d+)/balance/$', login_required(StockBalanceList.as_view()),
        name='stocks-stock-balance-list'),
)
