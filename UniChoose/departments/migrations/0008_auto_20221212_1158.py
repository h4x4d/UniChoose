# Generated by Django 3.2.16 on 2022-12-12 07:42
from threading import Thread

from django.db import migrations


def f(weighted_departments, departments, i):
    weighted_departments.objects.bulk_create([
        weighted_departments(
            id=department.id,
            vuz_rating=department.university.avg_rating,
            profile=int(department.profile_class.replace('.', '')),
            entry_score=department.entry_score,
            edu_level=department.edu_level,
            department_id=department.id,
        ) for department in departments.objects.all()[i:i + 500]
    ])


def create_weighted(apps, schema_editor):
    departments = apps.get_model('departments', 'Department')
    weighted_departments = apps.get_model('departments', 'WeightedDepartment')

    weighted_departments.objects.all().delete()

    for i in range(0, 17000, 500):
        th = Thread(target=f, args=[weighted_departments, departments, i])
        th.start()


class Migration(migrations.Migration):
    dependencies = [
        ('departments', '0007_auto_20221212_1158'),
    ]

    operations = [
        migrations.RunPython(create_weighted),
    ]
