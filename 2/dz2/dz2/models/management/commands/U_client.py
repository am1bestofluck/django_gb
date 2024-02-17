import pdb
from django.core.management.base import BaseCommand
from models.models import Client


class Command(BaseCommand):
    help = "меняем клиента по id"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("id", type=int)  # nargs="+" - собирает аргументы в список
        parser.add_argument("--name", type=str)
        parser.add_argument("--mail", type=str)
        parser.add_argument("--phone", type=str)
        parser.add_argument("--path", type=str)
        parser.add_argument("--date_reg", type=str)

    def handle(self, *args, **kwargs):
        pdb.set_trace()
        client = Client.objects.filter(pk=kwargs['id']).first()

        if not client:
            raise ValueError("nothing to edit.")
        self.stdout.write(f"b4: {client}")

        prev_arg = client.name
        # Easier to Ask Forgiveness Than Permission, python-дзен ^^ (часть первая)
        # получается сделал через try: если есть ключ то меняй, а иначе pass. А оно ложит туда None на выходе!!
        # обалдеск полный
        if kwargs['name']:
            client.name = kwargs['name']
        if kwargs['mail']:
            client.mail = kwargs['mail']
        if kwargs['phone']:
            client.phone = kwargs['phone']
        if kwargs['path']:
            client.path = kwargs['path']
        if kwargs['date_reg']:
            client.date_reg = kwargs['date_reg']
        client.save()
        self.stdout.write(f"after:{client}")
