from django.db import models


class CoreNameModel(models.Model):
    name = models.CharField(verbose_name='name', max_length=200)

    class Meta:
        abstract = True
