from django.views.generic import ListView, DetailView
from  django.shortcuts import render

from .models import *

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
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
