from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserModel(AbstractUser):
    JOBS_CHOICES = [
        ('C', 'CEO'),
        ('ET', 'English Teacher'),
        ('M', 'Marketer'),
        ('MA', 'Manager'),
        ('MT', 'Math Teacher'),
        ('AS', 'Assistant'),
        ('BT', 'Backend Teacher'),
        ('FT', 'Frontend Teacher'),
        ('SMM', 'SMM Teacher'),
        ('TT', 'Trading Teacher')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.BigIntegerField(default='+998', null=True, blank=True)
    job_type = models.CharField(max_length=5, choices=JOBS_CHOICES, default='AS', null=True, blank=True)
    date_employeed = models.DateTimeField(auto_now_add=True)
    salary = models.BigIntegerField(default=0)
    is_paid = models.BooleanField(null=True, blank=True)
    card_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        unique_together = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SalaryPaymentsModel(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payment')
    amount = models.BigIntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.amount = self.employee.salary
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.amount} sums to {self.employee}"
