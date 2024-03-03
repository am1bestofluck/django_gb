from django import forms
from . import models


class WareForm(forms.Form):
    def_attrs = {"class": "form_fields"}
    title = forms.CharField(widget=forms.TextInput(attrs=def_attrs))
    notes = forms.CharField(widget=forms.Textarea(attrs=def_attrs))
    price = forms.DecimalField(widget=forms.NumberInput(attrs=def_attrs))
    quantity = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs=def_attrs))
    date_income = forms.DateField(widget=forms.DateInput(attrs=def_attrs))
    front_view = forms.ImageField(widget=forms.FileInput(attrs=def_attrs))

    def add_context(self, ware: models.Ware) -> None:
        self.fields['title'].initial = ware.title
        self.fields['notes'].initial = ware.notes
        self.fields['price'].initial = ware.price
        self.fields['quantity'].initial = ware.quantity
        self.fields['date_income'].initial = ware.date_income
        self.fields['front_view'].initial = f"{ware.front_view}"
        return None
