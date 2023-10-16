from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class CoursesModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.BigIntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class GroupsModel(models.Model):
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE,related_name='groups')
    WEEKDAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    days = ArrayField(
        models.CharField(max_length=10, choices=WEEKDAYS_CHOICES),
        default=[],
    )
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.TimeField()


class StudentsModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    group = models.ForeignKey(GroupsModel, on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PaymentsModel(models.Model):
    student = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, related_name='payments')
    amount = models.BigIntegerField()

    def __str__(self):
        return f"{self.student} has paid {self.amount} sums"
