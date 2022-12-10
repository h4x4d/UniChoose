from django.contrib.auth.models import AbstractUser
from django.db import models
from universities.models import University
from departments.models import Department


class Account(AbstractUser):
    liked_unis = models.ManyToManyField(
        University, verbose_name='liked universities')
    liked_dpts = models.ManyToManyField(
        Department, verbose_name='liked departments')

    def __str__(self):
        return self.username


class AccountDepartmentRelations(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name='account')
    department = models.OneToOneField(
        Department, on_delete=models.CASCADE, related_name='department')
    strength = models.PositiveSmallIntegerField(
        verbose_name='relation strength')
