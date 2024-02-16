import pdb

from django.core.management.base import BaseCommand
from blog_models.models import Author, Article


class Command(BaseCommand):
    help = "рандомим по qua статей для каждого автора"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("qua", type=int)  # nargs="+" - собирает аргументы в список

    def handle(self, *args, **kwargs):
        authors = list(Author.objects.all())
        qua = kwargs['qua']
        pdb.set_trace()
        for author in authors:
            for article_number in range(1, qua + 1, 1):
                article = Article(

                )
