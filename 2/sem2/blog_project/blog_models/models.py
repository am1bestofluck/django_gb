from django.db.models import (Model, CharField, EmailField, TextField,
                              DateField, ForeignKey, CASCADE, IntegerField)
from datetime import datetime, timedelta
from random import choice
from django.utils import lorem_ipsum


# Create your models here.

class Author(Model):
    name, surname = CharField(max_length=100), CharField(max_length=100)
    email = EmailField()
    bio = TextField(default=lorem_ipsum.words(count=20, common=False))
    birt_date = DateField(default=(datetime.now()
                                   - timedelta(weeks=4 * 12 * choice(range(5, 95))))
                          .date()
                          .strftime("%Y-%m-%d"))
    full_name = CharField(max_length=200, blank=True, default="")

    def save(self, *args, **kwargs):
        # https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
        self.full_name = f"{self.name} {self.surname}"
        super(Author, self).save(*args, **kwargs)


class Article(Model):
    title = CharField(max_length=200, default=lorem_ipsum.words(count=5, common=False))
    content = TextField(lorem_ipsum.words(count=20, common=False))
    publication_date = DateField((datetime.now()
                                  - timedelta(weeks=4 * choice(range(5, 95))))
                                 .date()
                                 .strftime("%Y-%m-%d"))
    author = ForeignKey(Author, on_delete=CASCADE)
    tags = CharField(max_length=100, default=lorem_ipsum.words(count=3, common=False))
    views = IntegerField(default=0)
