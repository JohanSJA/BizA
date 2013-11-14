from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.formtools.wizard.views import SessionWizardView

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
    return HttpResponse(io.getvalue(), content_type='image/svg+xml')


class ProductPrintingView(DetailView):
    model = Product
    template_name = 'stocks/product_printing.html'


class ItemCreateView(CreateView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item


class PackageCreateWizardView(SessionWizardView):
    form_list = [PackageForm1, PackageForm2]
    template_name = 'stocks/package_wizard_form.html'
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Package()
        return self.instance

    def done(self, form_list, **kwargs):
        pkg = self.instance
        pkg.save()
        return redirect(pkg.get_absolute_url())


class PackageUpdateWizardView(PackageCreateWizardView):
    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Package.objects.get(pk=self.kwargs['pk'])
        return self.instance
