import pdb

from django.core.management.base import BaseCommand
from models.models import Client


class Command(BaseCommand):
    help = "читаем всех клиентов, ну или одного по id"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("--qua", type=int)  # nargs="+" - собирает аргументы в список

    def handle(self, *args, **kwargs):
        # pdb.set_trace()
        if not kwargs['qua']:
            clients = Client.objects.all()
            self.stdout.write(str(clients))
            exit(0)
        self.stdout.write(f"{Client.objects.filter(pk=kwargs['qua']).first()}")
