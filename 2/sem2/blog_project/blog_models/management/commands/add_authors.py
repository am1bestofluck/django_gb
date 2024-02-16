import pdb

from django.core.management.base import BaseCommand
from blog_models.models import Author


class Command(BaseCommand):
    help = "рандомим авторов"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("qua", type=int)  # nargs="+" - собирает аргументы в список

    def handle(self, *args, **kwargs):
        # pdb.set_trace()
        qua = kwargs['qua']
        for i in range(qua):
            author = Author(
                name=f"name#{i}",
                surname=f"surname#{i}",
                email=f"mail#{i}@fake_mail.domain"
            )
            author.save()
