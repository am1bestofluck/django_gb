import pdb

from django.core.management.base import BaseCommand
from blog_models.models import Author, Comment, Article
from random import choice


class Command(BaseCommand):
    help = "рандомим комментарии; вывод 0 - всё получилось"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("qua", type=int)  # nargs="+" - собирает аргументы в список

    def handle(self, *args, **kwargs):
        pdb.set_trace()
        qua = kwargs['qua']
        authors = [*Author.objects.all()]
        articles = [*Article.objects.all()]
        for i in range(qua):
            comment = Comment(author=choice(authors), article=choice(articles))
            comment.save()
        self.stdout.write("0")

    # author = ForeignKey(Author, on_delete=DO_NOTHING)
    # article = ForeignKey(Article, on_delete=DO_NOTHING)
    # content = TextField(default=lorem_ipsum.words(count=20, common=False))
    # date_created = DateTimeField(
    #     default=(datetime.now()
    #              - timedelta(weeks=4 * choice(range(1, 4)))).strftime("%Y-%m-%d  %H:%M"))
    # date_edited = DateField(auto_now_add=True)
