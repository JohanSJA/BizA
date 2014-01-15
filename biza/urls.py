from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

from .views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^stocks/', include('stocks.urls')),

    url(r'^$', login_required(Home.as_view()), name='home'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
