from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from products.models import Product, Component, Quantity
from products.forms import ComponentForm, QuantityForm


class ProductLv(ListView):
    model = Product

class ProductDv(DetailView):
    model = Product

class ProductCv(CreateView):
    model = Product

class ProductUv(UpdateView):
    model = Product

class ComponentCv(CreateView):
    form_class = ComponentForm
    template_name = 'products/component_form.html'

    def get_context_data(self, **kwargs):
        context = super(ComponentCv, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['product_pk'])
        return context

    def get_form(self, form_class):
        form = super(ComponentCv, self).get_form(form_class)
        form.instance.product = Product.objects.get(pk=self.kwargs['product_pk'])
        return form

    def get_success_url(self):
        return self.object.product.get_absolute_url()

class QuantityCreateView(CreateView):
    form_class = QuantityForm
    template_name = 'products/quantity_form.html'

    def get_context_data(self, **kwargs):
        context = super(QuantityCreateView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['product_pk'])
        return context

    def get_form(self, form_class):
        form = super(QuantityCreateView, self).get_form(form_class)
        form.instance.product = Product.objects.get(pk=self.kwargs['product_pk'])
        return form

    def form_valid(self, form):
        product = form.instance.product
        warehouse = form.instance.warehouse
        changes = form.instance.changes
        quantities = Quantity.objects.filter(product=product, warehouse=warehouse)
        if quantities:
            last_quantity = quantities.last()
            balance = last_quantity.balance + changes
        else:
            balance = changes
        form.instance.balance = balance
        return super(QuantityCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.product.get_absolute_url()
