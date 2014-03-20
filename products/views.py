from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Uom, Category, Product


class UomListView(ListView):
    model = Uom
    paginate_by = 25


class UomDetailView(DetailView):
    model = Uom

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uom = self.get_object()
        context['product_list'] = uom.product_set.all()
        return context


class UomCreateView(CreateView):
    model = Uom


class UomUpdateView(UpdateView):
    model = Uom


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['product_list'] = category.product_set.all()
        return context


class CategoryCreateView(CreateView):
    model = Category
    success_url = reverse_lazy('products_category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    success_url = reverse_lazy('products_category_list')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
