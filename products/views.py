from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import Category, Uom, Product, Pricelist


class ProductHomeView(TemplateView):
    template_name = "products/home.html"


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category

class CategoryUpdateView(UpdateView):
    model = Category


class UomListView(ListView):
    model = Uom

class UomDetailView(DetailView):
    model = Uom

class UomCreateView(CreateView):
    model = Uom
    template_name = "base_form.html"

class UomUpdateView(UpdateView):
    model = Uom
    template_name = "base_form.html"


class ProductListView(ListView):
    model = Product
    template_name = "base_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "base_detail.html"

class ProductCreateView(CreateView):
    model = Product
    template_name = "base_form.html"

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "base_form.html"


class PricelistListView(ListView):
    model = Pricelist
    template_name = "base_list.html"

class PricelistDetailView(DetailView):
    model = Pricelist
    template_name = "base_detail.html"

class PricelistCreateView(CreateView):
    model = Pricelist
    template_name = "base_form.html"

class PricelistUpdateView(UpdateView):
    model = Pricelist
    template_name = "base_form.html"
