from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    desc = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=True)
    def __str__(self):
        return "{}-{}".format(self.desc, self.date)

class Income(models.Model):
    desc = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=True)
    def __str__(self):
        return "{}-{}".format(self.desc, self.date)


