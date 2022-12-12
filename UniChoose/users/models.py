from departments.models import Department
from django.contrib.auth.models import AbstractUser
from django.db import models
from universities.models import University


class Account(AbstractUser):
    liked_unis = models.ManyToManyField(University,
                                        verbose_name='liked universities')
    liked_dpts = models.ManyToManyField(Department,
                                        verbose_name='liked departments')

    def __str__(self):
        return self.username


class AccountDepartmentRelations(models.Model):
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='relations')
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name='relations')
    strength = models.PositiveSmallIntegerField(
        verbose_name='relation strength')


class Subject(models.Model):
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='subjects')
    name = models.CharField(max_length=50)
