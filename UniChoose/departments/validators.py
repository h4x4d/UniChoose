import re

from django.core.exceptions import ValidationError


def validate_department_classification_format(value):
    if re.match(r'^[0-9]{2}.[0-9]{2}.[0-9]{2}$', value) is None:
        raise ValidationError(
            'Profile classification is not matching proper format')
