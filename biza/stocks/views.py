from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import *

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = self.get_object()
        try:
          employee = self.request.user.employee
          if employee.work_in_hq():
              context['quantities'] = product.item.itemquantity_set.all()
          else:
              context['quantities'] = product.item.itemquantity_set.filter(warehouse=employee.store.warehouse)
        except Product.DoesNotExist:
          pass
        return context

class ItemCreateView(CreateView):
    model = Item

class ItemUpdateView(UpdateView):
    model = Item

class PackageCreateView(CreateView):
    model = Package

class PackageUpdateView(UpdateView):
    model = Package
