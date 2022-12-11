# Generated by Django 3.2.16 on 2022-12-11 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_delete_accountdepartmentrelations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='entry_score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(311)], verbose_name='minimal entry exam score'),
        ),
    ]