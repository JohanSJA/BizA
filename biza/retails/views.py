from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import *
from .forms import *

class SaleListView(ListView):
    model = Sale

class SaleCreateView(CreateView):
    form_class = SaleForm
    template_name = 'retails/sale_form.html'

    def form_valid(self, form):
        form.instance.store = self.request.user.employee.store
        return super(SaleCreateView, self).form_valid(form)

class SaleDetailView(DetailView):
    model = Sale

    def get_context_data(self, **kwargs):
        context = super(SaleDetailView, self).get_context_data(**kwargs)
        context['lines'] = self.get_object().saleline_set.all()
        return context

class SaleUpdateView(UpdateView):
    form_class = SaleForm
    template_name = 'retails/sale_form.html'

    def get_object(self, queryset=None):
        return Sale.objects.get(pk=self.kwargs['pk'])

class SaleLineListView(ListView):
    model = SaleLine

class SaleLineCreateView(CreateView):
    model = SaleLine

class SaleLineDetailView(DetailView):
    model = SaleLine

class SaleLineUpdateView(UpdateView):
    model = SaleLine
