from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('retails.views',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^biza/', include('biza.foo.urls')),
    url(r'^sale/$', login_required(SaleListView.as_view()), name='retails_sale_list'),
    url(r'^sale/new/$', login_required(SaleCreateView.as_view()), name='retails_sale_new'),
    url(r'^sale/(?P<pk>\d+)/$', login_required(SaleDetailView.as_view()), name='retails_sale_detail'),
    url(r'^sale/(?P<pk>\d+)/edit/$', login_required(SaleUpdateView.as_view()), name='retails_sale_edit'),
    url(r'^sale/(?P<pk>\d+)/close/$', login_required(SaleCloseView.as_view()), name='retails_sale_close'),
    url(r'^sale/(?P<pk>\d+)/quote/$', login_required(SaleQuoteView.as_view()), name='retails_sale_quote'),
    url(r'^sale/(?P<pk>\d+)/print/$', login_required(SalePrintView.as_view()), name='retails_sale_print'),
    url(r'^saleline/$', login_required(SaleLineListView.as_view()), name='retails_saleline_list'),
    url(r'^saleline/new/$', login_required(SaleLineCreateView.as_view()), name='retails_saleline_new'),
    url(r'^saleline/(?P<pk>\d+)/$', login_required(SaleLineDetailView.as_view()), name='retails_saleline_detail'),
    url(r'^saleline/(?P<pk>\d+)/edit/$', login_required(SaleLineUpdateView.as_view()), name='retails_saleline_edit'),
)
