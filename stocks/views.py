from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import *


class UnitList(ListView):
    model = Unit


class UnitCreate(CreateView):
    model = Unit
    success_url = reverse_lazy('stocks-unit-list')


class UnitUpdate(UpdateView):
    model = Unit
    success_url = reverse_lazy('stocks-unit-list')
