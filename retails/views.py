from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from retails.models import Price


class RetailTv(TemplateView):
    template_name = 'retails/home.html'


class PriceLv(ListView):
    model = Price

    def get_queryset(self):
        user_branch = self.request.user.employee.employee.branch
        return Price.objects.filter(branch=user_branch)
