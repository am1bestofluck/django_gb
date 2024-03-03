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
                    author=author

                )
                article.save()
                # title = CharField(max_length=200, default=lorem_ipsum.words(count=5, common=False))
                # content = TextField(lorem_ipsum.words(count=20, common=False))
                # publication_date = DateField((datetime.now()
                #                               - timedelta(weeks=4 * choice(range(5, 95))))
                #                              .date()
                #                              .strftime("%Y-%m-%d"))
                # author = ForeignKey(Author, on_delete=CASCADE)
                # tags = CharField(max_length=100, default=lorem_ipsum.words(count=3, common=False))
                # views = IntegerField(default=0)
