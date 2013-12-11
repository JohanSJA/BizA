from django.conf.urls import patterns, include, url

from employees.views import DashboardTv

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^biza/', include('biza.foo.urls')),
    url(r'dashboard/$', DashboardTv.as_view(), name='employees_dashboard'),
)
