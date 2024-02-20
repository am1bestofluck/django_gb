import pdb
from copy import deepcopy
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from models.models import Client, Ware, Order


class Command(BaseCommand):
    help = "вписываем заказы для 3-его дз:"
    "5 и 6 дней назад;"
    "20 и 22 дня назад; 50 и 52 дня назад;"
    "каждый заказ должен содержать уникальные и повторяющиеся лоты"
    "в рамках своего диапазона дат"
    "клиент #1"

    def handle(self, *args, **kwargs):
        # делаем списки товаров, ключ - timedelta, значения - списки индексов товаров
        purchase_event = dict()
        shared = [1, 2, 3]
        purchase_event[5] = deepcopy(shared)
        purchase_event[5].extend([4, 5])
        purchase_event[7] = deepcopy(shared)
        purchase_event[7].extend([6, 7])
        purchase_event[20] = deepcopy(purchase_event[5])
        purchase_event[20].extend([8, 9])
        purchase_event[22] = deepcopy(purchase_event[7])
        purchase_event[22].extend([10, 11])
        purchase_event[50] = deepcopy(purchase_event[20])
        purchase_event[50].extend([12, 13])
        purchase_event[52] = deepcopy(purchase_event[22])
        purchase_event[52].extend([14, 15])
        # pdb.set_trace()
        client: Client = Client.objects.get(pk=1)
        for timedelta_ in purchase_event:
            event_date = date.today() - timedelta(days=timedelta_)
            wares_list = [Ware.objects.get(pk=i) for i in purchase_event[timedelta_]]
            total = sum([i.price for i in wares_list])
            # pdb.set_trace()
            order = Order(client=client, total=total, date_locked=event_date.strftime("%Y-%m-%d"))
            order.save()
            order.wares.set(wares_list)
            order.save()
            print(f"{order}_saved!")
        self.stdout.write("0")
    #       client = ForeignKey(Client, on_delete=DO_NOTHING)
    #       wares = ManyToManyField(Ware, default=[], blank=True)
    #       total = IntegerField(default=0)  # формула тут, переопределить save.Но в тз не сказали.
    #       date_locked = DateField(auto_now=True)
