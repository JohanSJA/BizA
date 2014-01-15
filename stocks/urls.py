from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'unit/$', login_required(UnitList.as_view()),
        name='stocks-unit-list'),
    url(r'unit/new/$', login_required(UnitCreate.as_view()),
        name='stocks-unit-new'),
    url(r'unit/(?P<pk>\d+)/edit/$', login_required(UnitUpdate.as_view()),
        name='stocks-unit-edit'),
)