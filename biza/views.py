from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'biza/home.html'


class Dashboard(TemplateView):
    template_name = 'biza/dashboard.html'
