from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

from biza.views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^$", Home.as_view(), name="home"),

    url(r"^login/$", "django.contrib.auth.views.login", name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),

    url(r"^products/", include("products.urls")),

    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns("",
        (r"^static/(?<path>.*)$", "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
    )
