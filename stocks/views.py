from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Uom, Warehouse, Stock, Log


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



class StockListView(LoginRequiredMixin, ListView):
    model = Stock


class StockDetailView(LoginRequiredMixin, DetailView):
    model = Stock


class StockCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'auth.add_stock'
    raise_exception = True

    model = Stock


class StockUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_stock'
    raise_exception = True

    model = Stock
