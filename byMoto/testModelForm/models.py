from django.db import models
from datetime import date

class TestData(models.Model):

    LEVELS = [(x,str(x)) for x in range(1, 17)]

    dName         = models.CharField(max_length=30,     default='data_name')
    dDescription  = models.CharField(max_length=300,    default='data_description')
    dLevel        = models.IntegerField(choices=LEVELS, default=11)
    dDate         = models.DateField(auto_now=False,    default=date.today)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.dName