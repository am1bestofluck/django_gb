import pdb

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import Client, Ware, Order

from datetime import date, timedelta
from . import models
from . import forms


# Create your views here.

class OrderLog(TemplateView):
    template_name = "models/order_log.html"
    semantic_name = "Product demand report"

    def get_context_data(self, **kwargs):
        """
        1) находим заказы клиента
        2) бьём дату по трём критериям;
        3) если входит - добавляем единичку в словарь вывода по первичному ключу
        :param kwargs:
        :return:
        """
        
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(pk=kwargs['customer_id'])
        periods = {'week': 7,
                   'month': 30,
                   'year': 365}

        temp = dict()
        for per in periods:
            temp[per] = Order.objects.filter(date_locked__gte=date.today() - timedelta(days=periods[per]))
            context.setdefault(per, dict())

        for ware_set in temp:
            for query in temp[ware_set]:
                for ware in query.wares.all():
                    context[ware_set].setdefault(ware.title, 0)
                    context[ware_set][ware.title] += 1
        

        context['title'] = f"{self.semantic_name} for  {client.name}"
        context['title__verbosed'] = context['title']
        return context


def index(request):
    # return redirect("order_log", customer_id=1)
    return redirect("r_u_ware", ware_id=1)


class EditWare(View):
    template_name = "models/edit_ware.html"

    def get(self, request, ware_id):
        ware = models.Ware.objects.get(pk=ware_id)
        
        context = {f"verbose_title": "RW of  {ware}"}
        buffer = forms.WareForm()
        buffer.add_context(ware)
        context['form'] = buffer
        context['ware_descr'] = ware.full_description()
        context['img_path'] = ware.front_view.url
        return render(request, self.template_name, context=context)

    def post(self, request, ware_id):
        form = forms.WareForm(request.POST, request.FILES)
        
        if form.is_valid():
            prev = models.Ware.objects.get(pk=ware_id)
            prev.title = form.cleaned_data['title']
            prev.notes = form.cleaned_data['notes']
            prev.price = form.cleaned_data['price']
            prev.quantity = form.cleaned_data['quantity']
            prev.front_view = form.cleaned_data['front_view']
            # file_storage = FileSystemStorage()
            # file_storage.save(form.cleaned_data['front_view'].name, form.cleaned_data['front_view'])
            prev.save()
        else:
            return HttpResponse(form.errors)
        return redirect("r_u_ware", ware_id=ware_id)
