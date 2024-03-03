import pdb

from django.db import models


# Create your models here.

class CoinLogger(models.Model):
    result = models.BooleanField()
    toss_time = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_newest(qua: int):
        out = {True: 0, False: 0}
        all_ = list(CoinLogger.objects.all())[-qua:]
        for i in all_:
            out[i.result] += 1
        # pdb.set_trace()
        return out

    def __str__(self):
        return f"coinToss: {'face' if self.result else 'rear'} at {self.toss_time}"
