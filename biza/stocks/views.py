from django.views.generic import ListView
from  django.shortcuts import render

from .models import *

class ProductList(ListView):
    model = Product
