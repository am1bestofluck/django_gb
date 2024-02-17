import pdb
from sys import exit
from django.core.management.base import BaseCommand
from blog_models.models import Author, Article


class Command(BaseCommand):
    help = "\n".join(["Article_crUd; by article id;",
                      "use_case: Article_update 1",
                      "exit code 0 for success",
                      "exit code 1 if id not recognized",
                      "exit code 2 if no valid edits were passed"
                      ])

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("Article_id", type=int)
        # Named (optional) arguments
        parser.add_argument(
            "--title",
            help="passing new title content")
        parser.add_argument(
            "--content",
            help="passing new content of content field")
        parser.add_argument(
            "--publication_date",
            help="passing new publication_date content")
        parser.add_argument(
            "--author",
            help="passing new author(by id) content")
        parser.add_argument(
            "--tags",
            help="passing new tags content")
        parser.add_argument(
            "--views",
            help="passing new views content")

    def handle(self, *args, **kwargs_as_optionals):
        art_id = kwargs_as_optionals['Article_id']

        read_target: Article = Article.objects.filter(id=art_id).first()
        if (not kwargs_as_optionals['title'] and not kwargs_as_optionals['content'] and not kwargs_as_optionals[
            'publication_date'] and not kwargs_as_optionals['author'] and not kwargs_as_optionals['tags']) \
                and not kwargs_as_optionals['views']:
            self.stderr.write('no valid edits were passed')
            exit(2)
        if not read_target:
            self.stderr.write('1')
            exit(1)
        pdb.set_trace()
        self.stdout.write(f"old: {read_target}")
        if kwargs_as_optionals["title"]:
            read_target.title = kwargs_as_optionals["title"]
        if kwargs_as_optionals["content"]:
            read_target.content = kwargs_as_optionals["content"]
        if kwargs_as_optionals["publication_date"]:
            read_target.publication_date = kwargs_as_optionals["publication_date"]
        if kwargs_as_optionals["author"]:
            read_target.author = Author.objects.filter(id=kwargs_as_optionals["author"]).first()
        if kwargs_as_optionals["tags"]:
            read_target.tags = kwargs_as_optionals["tags"]
        if kwargs_as_optionals["views"]:
            read_target.views = kwargs_as_optionals["views"]

        read_target.save()
        self.stdout.write(f"new: {read_target}")
        exit(0)

    # title = CharField(max_length=200, default=lorem_ipsum.words(count=5, common=False))
    # content = TextField(default=lorem_ipsum.words(count=20, common=False))
    # publication_date = DateField(default=(datetime.now()
    #                                       - timedelta(weeks=4 * choice(range(5, 95))))
    #                              .date()
    #                              .strftime("%Y-%m-%d"))
    # author = ForeignKey(Author, on_delete=CASCADE)
    # tags = CharField(max_length=100, default=lorem_ipsum.words(count=3, common=False))
    # views = IntegerField(default=0)
