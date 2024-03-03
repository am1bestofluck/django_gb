import pdb

from django.core.management.base import BaseCommand
from models.models import Client, Ware, Order
from datetime import date


class Command(BaseCommand):
    help = "рандомим заказы [id клиента] [через пробел товары в заказе]"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("cli_id", type=int)  # nargs="+" - собирает аргументы в список; даёт ошибку если пусто
        parser.add_argument("ware_ids", type=int, nargs="*")

    def handle(self, *args, **kwargs):
        client: Client = Client.objects.get(pk=kwargs['cli_id'])
        wares = kwargs["ware_ids"]
        # pdb.set_trace()
        wares_list = [Ware.objects.filter(pk=i).first() for i in wares]
        total = sum([i.price for i in wares_list])
        if None in wares_list:
            raise ValueError("не все товары опознаны")
        order = Order(client=client, total=total, date_locked=date.today())
        order.save()
        for ware_ in wares_list:
            order.wares.add(ware_)
        order.save()
        self.stdout.write("0")
#       client = ForeignKey(Client, on_delete=DO_NOTHING)
#       wares = ManyToManyField(Ware, default=[], blank=True)
#       total = IntegerField(default=0)  # формула тут, переопределить save.Но в тз не сказали.
#       date_locked = DateField(auto_now=True)
