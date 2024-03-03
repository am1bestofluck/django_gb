import pdb

from django.db.models import (Model, CharField, EmailField, TextField,
                              DateField, DateTimeField, ForeignKey, CASCADE, IntegerField, DO_NOTHING, SET_NULL,
                              BooleanField, Field)
from datetime import datetime, timedelta
from random import choice
from django.utils import lorem_ipsum


# Create your models here.

class Author(Model):
    name, surname = CharField(max_length=100), CharField(max_length=100)
    email = EmailField()
    bio = TextField(default=lorem_ipsum.words(count=20, common=False))
    birth_date = DateField(default=(datetime.now()
                                    - timedelta(weeks=4 * 12 * choice(range(5, 95))))
                           .date()
                           .strftime("%Y-%m-%d"))
    full_name = CharField(max_length=200, blank=True, default="", null=True)

    def save(self, *args, **kwargs):
        # https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
        self.full_name = f"{self.name} {self.surname}"
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__} #{self.pk};{self.full_name}, mail: {self.email}"

    def __ge__(self, other):
        return self.pk >= other.pk

    def __eq__(self, other):
        # pdb.set_trace()
        if other is None:
            return False
        if not isinstance(other, Author):
            return False
        return self.pk == other.pk

    def __lt__(self, other):
        return self.pk < other.pk


class Article(Model):
    title = CharField(max_length=200, default=lorem_ipsum.words(count=5, common=False))
    content = TextField(default=lorem_ipsum.words(count=20, common=False))
    publication_date = DateField(default=(datetime.now()
                                          - timedelta(weeks=4 * choice(range(5, 95))))
                                 .date()
                                 .strftime("%Y-%m-%d"))
    author = ForeignKey(Author, on_delete=CASCADE)
    tags = CharField(max_length=100, default=lorem_ipsum.words(count=3, common=False))
    views = IntegerField(default=0)
    isPublished = BooleanField(default=True)

    def __ge__(self, other):
        return self.pk >= other.pk

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.pk == other.pk

    def __lt__(self, other):
        return self.pk < other.pk

    def __str__(self):
        return f"{self.__class__.__name__} '{self.title}' #{self.pk}, author: {self.author.full_name}, published at {self.publication_date}"

    def intro(self):
        return " ".join(self.content.split()[:10]) + "..."


class Comment(Model):
    author: Author = ForeignKey(Author, on_delete=DO_NOTHING)
    article: Article = ForeignKey(Article, on_delete=DO_NOTHING)
    content = TextField(default=lorem_ipsum.words(count=20, common=False))
    date_created = DateTimeField(
        default=(datetime.now()
                 # - timedelta(weeks=4 * choice(range(1, 4)))).strftime("%Y-%m-%d %H:%M"))
                 - timedelta(weeks=4 * choice(range(1, 4)))))  ##.strftime("%Y-%m-%d %H:%M"))
    date_edited = DateField(auto_now_add=True, null=True)

    def __ge__(self, other):
        return self.pk >= other.pk

    def __eq__(self, other):
        if other is None:
            return False
        return self.pk == other.pk

    def __lt__(self, other):
        return self.pk < other.pk

    def __str__(self):
        return f"{self.__class__.__name__}(#{self.pk}) from {self.author.full_name} about {self.article.title}"

    def __hash__(self):
        """Что бы работало удаление из админки"""
        return hash(str(self))
