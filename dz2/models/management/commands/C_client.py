import pdb

from django.core.management.base import BaseCommand
from models.models import Client


class Command(BaseCommand):
    help = "рандомим qua клиентов"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("qua", type=int)  # nargs="+" - собирает аргументы в список

    def handle(self, *args, **kwargs):
        qua = kwargs['qua']
        # pdb.set_trace()
        for n_client in range(qua):
            client = Client()
            client.save()
            self.stdout.write(f"{client}")