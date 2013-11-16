from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse

from cStringIO import StringIO
from barcode.codex import Code39

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39

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


def product_printing_pdf_view(request, pk):
    product = Product.objects.get(pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="print.pdf"'

    page_width = 205 * mm
    page_height = 134 * mm
    page_size = (page_width, page_height)
    tl_sticker = (3 * mm, 133.5 * mm)
    sticker_size = (38 * mm, 25 * mm)
    sticker_gap = 2 * mm

    p = canvas.Canvas(response, pagesize=page_size)

    p.setFontSize(size=7)
    code = code39.Standard39(product.barcode, barHeight=10 * mm, checksum=0, quiet=0)

    for row in range(5):
        for col in range(5):
            x = tl_sticker[0] + col * sticker_gap + col * sticker_size[0]
            y = tl_sticker[1] - row * sticker_gap - row * sticker_size[1]
            str_x_center = x + (sticker_size[0] / 2)
            str_y = y - 6.5 * mm
            p.drawCentredString(str_x_center, str_y, 'Cheantar Electronics')
            code_x = x + (sticker_size[0] - code.width) / 2
            code_y = y - 17.5 * mm
            code.drawOn(p, code_x, code_y)
            str_y = y - 20.5 * mm
            p.drawCentredString(str_x_center, str_y, product.barcode)

    p.showPage()
    p.save()

    return response


class ItemCreateView(CreateView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item


class PackageCreateView(CreateView):
    model = Package
    form_class = PackageInfoForm
    template_name = 'stocks/package_form.html'


class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageInfoForm
    template_name = 'stocks/package_form.html'


class PackagePriceUpdateView(UpdateView):
    model = Package
    form_class = PackagePriceForm
    template_name = 'stocks/package_price_form.html'


class PackageItemCreateView(CreateView):
    model = PackageItem
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
        return reverse('stocks_package_edit_price', kwargs={'pk': self.object.package.id })


class PackageItemUpdateView(UpdateView):
    model = PackageItem
    form_class = PackageItemForm
    template_name = 'stocks/packageitem_form.html'

    def get_context_data(self, **kwargs):
        context = super(PackageItemUpdateView, self).get_context_data(**kwargs)
        context['package'] = self.object.package
        return context

    def get_success_url(self):
        return reverse('stocks_package_edit_price', kwargs={'pk': self.object.package.id })


class ItemQuantityCreateView(CreateView):
    model = ItemQuantity
    form_class = ItemQuantityForm
    template_name = 'stocks/itemquantity_form.html'

    def get_context_data(self, **kwargs):
        context = super(ItemQuantityCreateView, self).get_context_data(**kwargs)
        context['item'] = Item.objects.get(pk=self.kwargs['item_pk'])
        return context

    def form_valid(self, form):
        item = Item.objects.get(pk=self.kwargs['item_pk'])
        form.instance.item = item
        return super(ItemQuantityCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.item.get_absolute_url()


class ItemQuantityStoreCreateView(ItemQuantityCreateView):
    form_class = ItemQuantityStoreForm

    def form_valid(self, form):
        item = Item.objects.get(pk=self.kwargs['item_pk'])
        form.instance.item = item
        warehouse = self.request.user.employee.store.warehouse
        form.instance.warehouse = warehouse
        return super(ItemQuantityStoreCreateView, self).form_valid(form)
