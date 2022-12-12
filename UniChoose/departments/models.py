from core.models import CoreNameModel
from departments.validators import validate_department_classification_format
from django.core.validators import MaxValueValidator
from django.db import models
from universities.models import University


class Department(CoreNameModel):
    profile = models.TextField(verbose_name='profile')
    profile_class = models.CharField(
        verbose_name='profile class',
        max_length=20,
        validators=(validate_department_classification_format, ),
    )
    entry_score = models.PositiveSmallIntegerField(
        verbose_name='minimal entry exam score',
        validators=(MaxValueValidator(311), ),
    )
    edu_level = models.PositiveSmallIntegerField(
        verbose_name='education level')
    ege_subjects = models.JSONField(verbose_name='required_ege_subjects')
    university = models.ForeignKey(University,
                                   on_delete=models.CASCADE,
                                   related_name='university')

    def __str__(self):
        return self.name


class WeightedDepartment(models.Model):
    entry_score = models.IntegerField()
    vuz_rating = models.DecimalField(
        verbose_name='average rating',
        max_digits=3,
        decimal_places=1,
        validators=(MaxValueValidator(10.0), ),
    )
    edu_level = models.IntegerField()
    profile = models.IntegerField()

    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.department.name} weighted'
