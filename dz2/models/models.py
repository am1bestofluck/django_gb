from django.db.models import (Model, CharField, EmailField, TextField,
                              DateField, DateTimeField, ForeignKey, CASCADE, IntegerField, DO_NOTHING, SET_NULL,
                              DecimalField, ManyToManyField, ImageField)
from datetime import datetime, timedelta, date
from random import choice, choices, random
from string import digits
from django.utils import lorem_ipsum
import pdb

# Create your models here.
# клиент, товар и заказ.

class Client(Model):
    name = CharField(max_length=100, default=lorem_ipsum.words(2, common=False).title())
    mail = EmailField(max_length=100,
                      default=f"{lorem_ipsum.words(1, common=False)}@{lorem_ipsum.words(1, common=False)}"
                              f".{lorem_ipsum.words(1, common=False)}")
    phone = CharField(max_length=30,
                      default=f"{''.join(choices(digits, k=3))}-{''.join(choices(digits, k=3))}-{''.join(choices(digits, k=3))}")
    path = CharField(max_length=200,
                     default=f"{lorem_ipsum.words(2, common=False)}{choice(range(100))}, ap.{choice(range(100))} ")
    date_reg = DateField(
        default=date(choice(range(2000, datetime.today().year)), choice(range(1, 12)), choice(range(1, 29))).strftime(
            "%Y-%m-%d"))

    def __str__(self):
        return f"{self.__class__.__name__} #{self.pk}. {self.name}."


class Ware(Model):
    title = CharField(max_length=100, default=lorem_ipsum.words(2, common=False).title())
    notes = CharField(max_length=100, default=lorem_ipsum.words(4, common=False).title())
    price = DecimalField(max_digits=9,
                         decimal_places=3, default=round(choice(range(1, 100_000)) + random(), 2))
    quantity = IntegerField(default=choice(range(100)))
    date_income = DateField(auto_now=True)
    front_view = ImageField(null=True, help_text="front view",
                            upload_to="")

    def __str__(self):
        return f"{self.__class__.__name__} #{self.pk}. {self.title}//{self.price}"

    def full_description(self):
        return [f"{self.title=}", f"{self.notes=}", f"{self.price=}", f"{self.quantity=}",
                f"{self.date_income=}"]


class Order(Model):
    client = ForeignKey(Client, on_delete=DO_NOTHING)
    wares = ManyToManyField(Ware, default=[], blank=True)
    total = DecimalField(default=0, decimal_places=2,
                         max_digits=10)  # формула тут, переопределить save.Но в тз не сказали.
    date_locked = DateField()

    def __str__(self):
        return f"Order #{self.pk} from {self.date_locked}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total = 0
        pdb.set_trace()
        super().save(*args, **kwargs)
