from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse

from cStringIO import StringIO
from barcode.codex import Code39

from .models import *
from .forms import *

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = self.get_object()
        try:
          employee = self.request.user.employee
          if employee.work_in_hq():
              context['quantities'] = product.item.itemquantity_set.all()
          else:
              context['quantities'] = product.item.itemquantity_set.filter(warehouse=employee.store.warehouse)
        except Product.DoesNotExist:
          pass
        return context

def product_barcode_svg(request, pk):
    p = Product.objects.get(pk=pk)
    bc = p.barcode

    io = StringIO()
    code = Code39(bc, add_checksum=False)
    code.write(io)
    return HttpResponse(io.getvalue(), mimetype='image/svg+xml')


class ProductPrintingView(DetailView):
    model = Product
    template_name = 'stocks/product_printing.html'


class ItemCreateView(CreateView):
    model = Item

class ItemUpdateView(UpdateView):
    model = Item

class PackageCreateView(CreateView):
    model = Package

class PackageUpdateView(UpdateView):
    model = Package


class PackageItemCreateView(CreateView):
    form_class = PackageItemForm
    template_name = 'stocks/packageitem_form.html'

    def get_context_data(self, **kwargs):
        context = super(PackageItemCreateView, self).get_context_data(**kwargs)
        context['package'] = Package.objects.get(pk=self.kwargs['package_pk'])
        return context

    def form_valid(self, form):
        package = Package.objects.get(pk=self.kwargs['package_pk'])
        form.instance.package = package
        return super(PackageItemCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.package.get_absolute_url()


class PackageItemUpdateView(UpdateView):
    form_class = PackageItemForm
    template_name = 'stocks/packageitem_form.html'

    def get_object(self, queryset=None):
        return PackageItem.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PackageItemUpdateView, self).get_context_data(**kwargs)
        context['package'] = self.get_object().package
        return context

    def get_success_url(self):
        return self.object.package.get_absolute_url()
