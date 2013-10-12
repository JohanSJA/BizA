from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('stocks.views',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^biza/', include('biza.foo.urls')),
    url(r'^$', login_required(ProductList.as_view()), name='stocks_product_list'),
    url(r'^(?P<pk>\d+)/$', login_required(ProductDetail.as_view()), name='stocks_product_detail')
)
