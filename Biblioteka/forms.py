from django import forms

from .models import *


class BookForm(forms.Form):
    ask = forms.CharField(label="ask")
    def clean_book(self):
        askk = self.cleaned_data['ask']
        return askk

