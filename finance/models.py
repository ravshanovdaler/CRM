from django.db import models


class Debts(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    repaying_date = models.DateField(null=True, blank=True)
    amount = models.BigIntegerField()

    def __str__(self):
        return self.name


class Expenses(models.Model):
    where_or_what = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    data = models.DateField(auto_now_add=True)
    amount = models.BigIntegerField()

    def __str__(self):
        return self.where_or_what
