from django.views.generic.base import TemplateView

from employees.models import Employee

class DashboardTv(TemplateView):
    template_name = 'employees/dashboard.html'
