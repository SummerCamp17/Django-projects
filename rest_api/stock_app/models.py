from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField(default=0)

    def __str__(self):
        return self.ticker
