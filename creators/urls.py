from django.conf.urls import patterns, url

from .views import PartnerWizardView


urlpatterns = patterns('',
    url(r'^partner/new/$', PartnerWizardView.as_view(), name='creators_partner_new'),
)
