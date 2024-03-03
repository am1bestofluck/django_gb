import pdb
from sys import exit
from django.core.management.base import BaseCommand
from blog_models.models import Author, Article


class Command(BaseCommand):
    help = "\n".join(["Article_cruD; by article id;",
                      "use_case: article_delete 1",
                      "exit code 0 for success",
                      "exit code 1 if id not recognized",
                      ])

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("article_id", type=int)

    def handle(self, *args, **kwargs):
        art_id = kwargs['article_id']
        # pdb.set_trace()
        kill_switch = Article.objects.filter(id=art_id).first()
        if not kill_switch:
            self.stderr.write('1')
            exit(1)
        kill_switch.delete()
        self.stdout.write('0')
        exit(0)
