from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy

from .models import *


class UnitList(ListView):
    model = Unit


class UnitCreate(SuccessMessageMixin, CreateView):
    model = Unit
    success_url = reverse_lazy('stocks-unit-list')
    success_message = '%(name)s was created successfully.'


class UnitUpdate(SuccessMessageMixin, UpdateView):
    model = Unit
    success_url = reverse_lazy('stocks-unit-list')
    success_message = '%(name)s was updated successfully.'
