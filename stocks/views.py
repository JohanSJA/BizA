from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Uom


class UomListView(ListView):
    model = Uom


class UomDetailView(DetailView):
    model = Uom


class UomCreateView(CreateView):
    model = Uom


class UomUpdateView(UpdateView):
    model = Uom
