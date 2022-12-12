# Generated by Django 3.2.16 on 2022-12-12 13:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0007_rename_new_region_university_region'),
        ('departments', '0009_alter_weighteddepartment_department'),
        ('users', '0004_auto_20221212_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='max_distance',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='account',
            name='region',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='users',
                to='universities.region'),
        ),
        migrations.AddField(
            model_name='subject',
            name='mark',
            field=models.PositiveSmallIntegerField(
                default=100,
                validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='liked_dpts',
            field=models.ManyToManyField(related_name='users',
                                         to='departments.Department',
                                         verbose_name='liked departments'),
        ),
        migrations.AlterField(
            model_name='account',
            name='liked_unis',
            field=models.ManyToManyField(related_name='users',
                                         to='universities.University',
                                         verbose_name='liked universities'),
        ),
    ]
