from django.contrib.auth.models import AbstractUser
from django.db import models

from departments.models import Department
from universities.models import University


class Account(AbstractUser):
    liked_unis = models.ManyToManyField(
        University, verbose_name='liked universities')
    liked_dpts = models.ManyToManyField(
        Department, verbose_name='liked departments')
    ege_marks = models.JSONField(verbose_name='ege marks',
                                 null=True, blank=False)

    def __str__(self):
        return self.username


class AccountDepartmentRelations(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account')
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='department')
    strength = models.PositiveSmallIntegerField(
        verbose_name='relation strength')
