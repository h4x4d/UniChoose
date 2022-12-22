from django.core.exceptions import ValidationError

from fixtures.regions_fixture import regions


def validate_distance(distance):
    if int(distance) < 0:
        raise ValidationError('Расстояние должно быть больше нуля')
    return True


def validate_region(region):
    if region not in regions:
        raise ValidationError('Введите существующий регион')
    return True


def validate_subject(subject):
    if subject > 100 or subject < 0:
        raise ValidationError('Введите корректные баллы за экзамены')
    return True
