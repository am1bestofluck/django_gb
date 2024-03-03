import pdb
from sys import exit
from django.core.management.base import BaseCommand
from blog_models.models import Author, Article


class Command(BaseCommand):
    help = "\n".join(["Author_cruD; by article id;",
                      "use_case: author_delete 1",
                      "exit code 0 for success",
                      "exit code 1 if id not recognized",
                      ])

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("author_id", type=int)

    def handle(self, *args, **kwargs):
        author_id = kwargs['author_id']
        # pdb.set_trace()
        kill_switch = Author.objects.filter(id=author_id).first()
        if not kill_switch:
            self.stderr.write('1')
            exit(1)
        kill_switch.delete()
        self.stdout.write('0')
        exit(0)