from django import forms


class StockCodePrintForm(forms.Form):
    start = forms.IntegerField(max_value=25, min_value=1, label='Starting sticker',
            help_text='Number is counted from top to bottom and left to right.')
    amount = forms.IntegerField(min_value=1, label='Total amount',
            help_text='Amount that you want to print.')
