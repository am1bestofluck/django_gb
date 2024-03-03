import pdb
from sys import exit
from django.core.management.base import BaseCommand
from blog_models.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Ищем по Article.title комментарии"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("title", type=str)
        parser.add_argument(
            "--comments",
            help="get n comments", type=int)
        parser.add_argument(
            "--sorted",
            action="store_true",
            help="сначала сортируем. По первичному ключу наверно."
        )

    def handle(self, *args, **options):
        title = options['title']
        article = Article.objects.filter(title=title).first()
        pdb.set_trace()
        if not options['comments']:
            self.stderr.write("No query specified")
            exit(2)
        sort_ = True if options['sorted'] else False
        items = abs(options['comments'])
        comments = [*Comment.objects.filter(article=article.pk)][:items]
        self.stdout.write(f"{sorted(comments) if sort_ else comments}")
        self.stdout.write("0")
