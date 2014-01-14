from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'unit/$', UnitList.as_view(), name='stocks-unit-list'),
    url(r'unit/new/$', UnitCreate.as_view(), name='stocks-unit-new'),
    url(r'unit/(?P<pk>\d+)/edit/$', UnitUpdate.as_view(), name='stocks-unit-edit'),
)
