import pdb

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class OrderLog(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pdb.set_trace()
        context[7] = dict()
        context[30] = dict()
        context[365] = dict()
        return context
