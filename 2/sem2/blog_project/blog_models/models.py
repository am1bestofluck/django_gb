from django.db.models import Model, CharField, EmailField, TextField, DateField
from datetime import datetime, timedelta
from random import choice


# Create your models here.

class Author(Model):
    name, surname = CharField(max_length=100), CharField(max_length=100)
    email = EmailField()
    bio = TextField()
    birt_date = ((datetime.now()
                  - timedelta(weeks=4 * 12 * choice(range(5, 95))))
                 .date()
                 .strftime("%Y-%m-%d"))

    def save(self, *args, **kwargs):
        # https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
        self.full_name = f"{self.name} {self.surname}"
        super(Author, self).save(*args, **kwargs)
