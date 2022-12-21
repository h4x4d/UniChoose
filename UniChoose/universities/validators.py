from django.core.exceptions import ValidationError
from fixtures.regions_fixture import regions


def validate_region(value):
    if value not in regions:
        raise ValidationError(f'{value} is not in region list')
