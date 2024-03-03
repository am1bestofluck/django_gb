import pdb
from sys import exit
from django.core.management.base import BaseCommand
from blog_models.models import Author, Article


class Command(BaseCommand):
    help = "\n".join(["Author_crUd; by author id;",
                      "use_case: Author_update 1",
                      "exit code 0 for success",
                      "exit code 1 if id not recognized",
                      "exit code 2 if no valid edits were passed"
                      ])

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("Author_id", type=int)
        # Named (optional) arguments
        parser.add_argument(
            "--mail",
            help="passing new email content")
        parser.add_argument(
            "--name",
            help="passing new name content")

        parser.add_argument(
            "--surname",
            help="passing new surname content")
        parser.add_argument(
            "--bio",
            help="passing new bio content")
        parser.add_argument(
            "--birth_date",
            help="passing new birthdate content")

    def handle(self, *args, **kwargs_as_optionals):
        art_id = kwargs_as_optionals['Author_id']

        read_target: Author = Author.objects.filter(id=art_id).first()
        if (not kwargs_as_optionals['name'] and not kwargs_as_optionals['surname'] and not kwargs_as_optionals['mail']
                and not kwargs_as_optionals['bio'] and not kwargs_as_optionals['birthdate']):
            self.stderr.write('no valid edits were passed')
            exit(2)
        if not read_target:
            self.stderr.write('1')
            exit(1)
        # pdb.set_trace()
        self.stdout.write(f"old: {read_target}")
        self.stdout.write(f'{read_target}')
        if kwargs_as_optionals["name"]:
            read_target.name = kwargs_as_optionals["name"]
        if kwargs_as_optionals["surname"]:
            read_target.surname = kwargs_as_optionals["surname"]
        if kwargs_as_optionals["mail"]:
            read_target.email = kwargs_as_optionals["mail"]
        if kwargs_as_optionals["bio"]:
            read_target.bio = kwargs_as_optionals["bio"]
        if kwargs_as_optionals["birth_date"]:
            read_target.birth_date = kwargs_as_optionals["birth_date"]
        read_target.save()
        self.stdout.write(f"new: {read_target}")
        exit(0)

        # name, surname = CharField(max_length=100), CharField(max_length=100)
        # email = EmailField()
        # bio = TextField(default=lorem_ipsum.words(count=20, common=False))
        # birth_date = DateField(default=(datetime.now()
        #                                - timedelta(weeks=4 * 12 * choice(range(5, 95))))
        #                       .date()
        #                       .strftime("%Y-%m-%d"))
