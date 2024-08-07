# Generated by Django 3.2.16 on 2022-12-12 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_alter_department_entry_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightedDepartment',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('entry_score', models.IntegerField()),
                ('vuz_rating', models.IntegerField()),
                ('edu_level', models.IntegerField()),
                ('profile', models.IntegerField()),
                ('department',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     to='departments.department')),
            ],
        ),
    ]
