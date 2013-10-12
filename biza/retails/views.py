from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import *

class SaleListView(ListView):
    model = Sale

class SaleCreateView(CreateView):
    model = Sale

class SaleDetailView(DetailView):
    model = Sale

    def get_context_data(self, **kwargs):
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['lines'] = self.get_object().saleline_set.all()
        return context

class SaleUpdateView(UpdateView):
    model = Sale

class SaleLineListView(ListView):
    model = SaleLine

class SaleLineCreateView(CreateView):
    model = SaleLine

class SaleLineDetailView(DetailView):
    model = SaleLine

class SaleLineUpdateView(UpdateView):
    model = SaleLine
