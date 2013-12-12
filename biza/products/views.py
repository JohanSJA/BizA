from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from products.models import Product


class ProductLv(ListView):
    model = Product

class ProductDv(DetailView):
    model = Product

class ProductCv(CreateView):
    model = Product

class ProductUv(UpdateView):
    model = Product
