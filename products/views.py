from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import Category


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
