from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.db import models

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39

from .models import *
from .forms import *


class StockList(ListView):
    model = Stock


class StockCreate(CreateView):
    model = Stock


class StockDetail(DetailView):
    model = Stock


class StockUpdate(UpdateView):
    model = Stock


class StockCodePrintCreate(FormView):
    template_name = 'stocks/stock_code_print_form.html'
    form_class = StockCodePrintForm

    def get_context_data(self, **kwargs):
        context = super(StockCodePrintCreate, self).get_context_data(**kwargs)
        context['stock'] = Stock.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        self._start = form.cleaned_data['start']
        self._amount = form.cleaned_data['amount']
        return super(StockCodePrintCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('stocks-stock-code-print-pdf', kwargs={
            'pk': self.kwargs['pk'], 'start': self._start, 'amount': self._amount
            })


def stock_code_print_pdf(request, pk, start, amount):
    stock = Stock.objects.get(pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="code_print.pdf"'

    page_width = 205 * mm
    page_height = 134 * mm
    page_size = (page_width, page_height)
    tl_sticker = (3 * mm, 133.5 * mm)
    sticker_size = (38 * mm, 25 * mm)
    sticker_gap = 2 * mm

    p = canvas.Canvas(response, pagesize=page_size)

    p.setFontSize(size=7)
    code = code39.Standard39(stock.code, barHeight=10 * mm, checksum=0, quiet=0)

    start = int(start)
    amount = int(amount)
    total = start + amount - 1 # total indicate blank sticker + print sticker
    sticker_row = 5
    sticker_col = 5
    num_col = total / sticker_row + 1
    last_row = total % sticker_row
    current_sticker = 1

    for col in range(num_col):
        col = col % sticker_col
        for row in range(sticker_row):
            if current_sticker >= start and current_sticker <= total:
                x = tl_sticker[0] + col * sticker_gap + col * sticker_size[0]
                y = tl_sticker[1] - row * sticker_gap - row * sticker_size[1]
                str_x_center = x + (sticker_size[0] / 2)
                str_y = y - 6.5 * mm
                p.drawCentredString(str_x_center, str_y, 'Cheantar Electronics')
                code_x = x + (sticker_size[0] - code.width) / 2
                code_y = y - 17.5 * mm
                code.drawOn(p, code_x, code_y)
                str_y = y - 20.5 * mm
                p.drawCentredString(str_x_center, str_y, stock.code)
            current_sticker += 1
        if col == 4 and current_sticker <= total:
            p.showPage()
            p.setFontSize(size=7)
            code = code39.Standard39(stock.code, barHeight=10 * mm, checksum=0, quiet=0)

    p.save()

    return response

class StockBalanceList(ListView):
    template_name = 'stocks/stock_balance_list.html'

    def get_queryset(self):
        stock = Stock.objects.get(pk=self.kwargs['stock_pk'])
        return Balance.objects.filter(stock=stock
                ).order_by('warehouse', '-timestamp').distinct('warehouse')

    def get_context_data(self, **kwargs):
        context = super(StockBalanceList, self).get_context_data(**kwargs)
        context['stock'] = Stock.objects.get(pk=self.kwargs['stock_pk'])

        balances = self.get_queryset()
        total_amount = 0
        for balance in balances:
            total_amount += balance.amount
        context['total_amount'] = total_amount

        return context
