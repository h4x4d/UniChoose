from core.models import CoreNameModel
from django.core.validators import MaxValueValidator
from django.db import models


class University(CoreNameModel):
    description = models.TextField(verbose_name='description',
                                   blank=True, null=True)
    avg_rating = models.DecimalField(verbose_name='average rating',
                                     max_digits=3, decimal_places=1,
                                     validators=(MaxValueValidator(10.0),),
                                     )
    rating_count = models.PositiveSmallIntegerField(
        verbose_name='rating count',
    )
    region = models.CharField(verbose_name='region',
                              max_length=100,
                              )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'university'
        verbose_name_plural = 'universities'
