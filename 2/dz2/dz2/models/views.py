import pdb

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Client, Ware, Order
from datetime import date, timedelta


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
        # pdb.set_trace()
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
        # pdb.set_trace()

        context['title'] = f"{self.semantic_name} for  {client.name}"
        context['title__verbosed'] = context['title']
        return context


def index(request):
    return redirect("order_log", customer_id=1)
