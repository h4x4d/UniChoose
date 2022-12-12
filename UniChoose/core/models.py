from django.core.validators import MaxValueValidator
from django.db import models


class CoreNameModel(models.Model):
    name = models.CharField(verbose_name='name', max_length=200)

    class Meta:
        abstract = True


class WeightedModel(models.Model):
    entry_score = models.IntegerField(blank=True, null=True)
    vuz_rating = models.DecimalField(
        verbose_name='average rating',
        max_digits=3,
        decimal_places=1,
        validators=(MaxValueValidator(10.0), ),
        blank=True,
        null=True,
    )
    edu_level = models.IntegerField(blank=True, null=True)
    profile = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
