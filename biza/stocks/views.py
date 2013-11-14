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

    def done(self, form_list, **kwargs):
        form1 = form_list[0]
        form2 = form_list[1]
        pkg = Package()
        pkg.model = form1.cleaned_data['model']
        pkg.name = form1.cleaned_data['name']
        pkg.barcode = form1.cleaned_data['barcode']
        pkg.retail_price = form2.cleaned_data['retail_price']
        pkg.lowest_retail_price = form2.cleaned_data['lowest_retail_price']
        pkg.wholesale_price = form2.cleaned_data['wholesale_price']
        pkg.lowest_wholesale_price = form2.cleaned_data['lowest_wholesale_price']
        pkg.save()
        return redirect('stocks_product_list')


class PackageUpdateWizardView(PackageCreateWizardView):
    def get_form_instance(self, step):
        return Package.objects.get(pk=self.kwargs['pk'])

    def done(self, form_list, **kwargs):
        form1 = form_list[0]
        form2 = form_list[1]
        pkg = Package.objects.get(pk=self.kwargs['pk'])
        pkg.model = form1.cleaned_data['model']
        pkg.name = form1.cleaned_data['name']
        pkg.barcode = form1.cleaned_data['barcode']
        pkg.retail_price = form2.cleaned_data['retail_price']
        pkg.lowest_retail_price = form2.cleaned_data['lowest_retail_price']
        pkg.wholesale_price = form2.cleaned_data['wholesale_price']
        pkg.lowest_wholesale_price = form2.cleaned_data['lowest_wholesale_price']
        pkg.save()
        return redirect('stocks_product_list')
