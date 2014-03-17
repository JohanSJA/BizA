from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Uom, Product


class UomListView(ListView):
    model = Uom
    paginate_by = 25


class UomCreateView(CreateView):
    model = Uom


class UomUpdateView(UpdateView):
    model = Uom


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
