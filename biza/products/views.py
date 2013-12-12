from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from products.models import Product

class ProductLv(ListView):
    model = Product

class ProductDv(DetailView):
    model = Product
