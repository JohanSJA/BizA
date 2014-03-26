from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Category, Product


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['product_list'] = category.product_set.all()
        return context


class CategoryCreateView(LoginRequiredMixin,
                         PermissionRequiredMixin,
                         CreateView):
    permission_required = 'auth.add_category'
    raise_exception = True

    model = Category


class CategoryUpdateView(LoginRequiredMixin,
                         PermissionRequiredMixin,
                         UpdateView):
    permission_required = 'auth.change_category'
    raise_exception = True

    model = Category


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
