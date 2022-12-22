import haversine as hs
from django.core.validators import MaxValueValidator
from django.db import models
from haversine import Unit

from core.models import CoreNameModel
from universities.validators import validate_region


class Region(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=200,
                            validators=[validate_region])
    latitude = models.FloatField()
    longitude = models.FloatField()

    def get_distance(self, other, unit=Unit.KILOMETERS):
        return hs.haversine((self.latitude, self.longitude),
                            (other.latitude, other.longitude),
                            unit=unit)

    def __str__(self):
        return self.name


class University(CoreNameModel):
    description = models.TextField(verbose_name='description',
                                   blank=True,
                                   null=True)
    avg_rating = models.DecimalField(
        verbose_name='average rating',
        max_digits=3,
        decimal_places=1,
        validators=(MaxValueValidator(10.0), ),
    )
    rating_count = models.PositiveSmallIntegerField(
        verbose_name='rating count')

    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               related_name='universities',
                               null=True,
                               blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'university'
        verbose_name_plural = 'universities'
