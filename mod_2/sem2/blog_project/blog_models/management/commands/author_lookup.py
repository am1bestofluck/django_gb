import pdb
from sys import exit
from django.core.management.base import BaseCommand
from blog_models.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Ищем по Author.name комментарии или статьи"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("name", type=str)
        parser.add_argument(
            "--comments",
            help="get n comments", type=int)
        parser.add_argument(
            "--articles",
            help="get n articles", type=int)
        parser.add_argument(
            "--sorted",
            action="store_true",
            help="сначала сортируем. По первичному ключу наверно."
        )

    def handle(self, *args, **options):
        name = options['name']
        author = Author.objects.filter(name=name).first()
        # pdb.set_trace()
        if not options['comments'] and not options['articles']:
            self.stderr.write("No query specified")
            exit(2)
        sort_ = True if options['sorted'] else False
        if options['comments']:
            items = abs(options['comments'])
            comments = [*Comment.objects.filter(author=author)][:items]
            self.stdout.write(f"{sorted(comments) if sort_ else comments}")
        if options['articles']:
            items = abs(options['articles'])
            articles = [*Article.objects.filter(author=author)][:items]
            self.stdout.write(f"{sorted(articles) if sort_ else articles}")
        self.stdout.write("0")
