from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    url(r'^price/$', login_required(PriceList.as_view()),
        name='retails-price-list'),
    url(r'^price/new/$', login_required(PriceCreate.as_view()),
        name='retails-price-new'),
    url(r'^price/(?P<pk>\d+)/edit/$', login_required(PriceUpdate.as_view()),
        name='retails-price-edit'),
)
