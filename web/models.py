from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Expense(models.Model):
    desc = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{}-{}".format(self.desc, self.date)

class Income(models.Model):
    desc = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{}-{}".format(self.desc, self.date)


class Token(models.Model):
    now = datetime.now()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=24)
    def __str__(self):
        return "{}-{}".format(self.now, self.user)


class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # TODO: do not save password