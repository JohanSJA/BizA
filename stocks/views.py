from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Uom, Warehouse, Category, Product, Log


class StockHomeView(TemplateView):
    template_name = 'stocks/home.html'


class UomListView(LoginRequiredMixin, ListView):
    model = Uom


class UomDetailView(LoginRequiredMixin, DetailView):
    model = Uom


class UomCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'auth.add_uom'
    raise_exception = True

    model = Uom


class UomUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_uom'
    raise_exception = True

    model = Uom


class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse


class WarehouseDetailView(LoginRequiredMixin, DetailView):
    model = Warehouse


class WarehouseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'auth.add_warehouse'
    raise_exception = True

    model = Warehouse


class WarehouseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_warehouse'
    raise_exception = True

    model = Warehouse



class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'auth.add_product'
    raise_exception = True

    model = Product


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_product'
    raise_exception = True

    model = Product


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
