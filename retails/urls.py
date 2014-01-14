from django.conf.urls import patterns, url

from retails.views import *


urlpatterns = patterns('',
    url(r'^$', RetailTv.as_view(), name='retails_home'),
    url(r'^prices/$', PriceLv.as_view(), name='retails_price_list'),
)
