# Generated by Django 3.2.16 on 2022-12-12 08:58

from django.db import migrations


def update_weighted(apps, schema_editor):
    departments = apps.get_model('departments', 'Department')

    for department in departments.objects.all():
        department.weighteddepartment.vuz_rating = \
            department.university.avg_rating


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0006_alter_weighteddepartment_vuz_rating'),
    ]

    operations = [
        migrations.RunPython(update_weighted),
    ]
