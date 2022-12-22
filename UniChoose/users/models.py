from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import CoreNameModel, WeightedModel
from departments.models import Department
from universities.models import Region


class Preference(WeightedModel):

    def __str__(self):
        return f'{self.user.username} preferences'


class Account(AbstractUser):
    max_distance = models.IntegerField(default=1000)

    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               related_name='users',
                               null=True,
                               blank=True)

    preference = models.OneToOneField(Preference,
                                      on_delete=models.CASCADE,
                                      related_name='user',
                                      null=True,
                                      blank=True)

    def __str__(self):
        return self.username


class AccountDepartmentRelations(models.Model):
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='relations')
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name='relations')
    strength = models.SmallIntegerField(verbose_name='relation strength')


class Subject(CoreNameModel):
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='subjects')
    mark = models.PositiveSmallIntegerField(
        default=100, validators=(MaxValueValidator(100), ))

    def __str__(self):
        return self.name
