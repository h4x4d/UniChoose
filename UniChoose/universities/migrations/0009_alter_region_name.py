# Generated by Django 3.2.16 on 2022-12-21 17:17

from django.db import migrations, models

import universities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0008_auto_20221212_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(
                max_length=200,
                validators=[universities.validators.validate_region],
                verbose_name='name'),
        ),
    ]