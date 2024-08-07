# Generated by Django 3.2.16 on 2022-12-11 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_alter_department_entry_score'),
        ('users', '0002_auto_20221210_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdepartmentrelations',
            name='account',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='account',
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountdepartmentrelations',
            name='department',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='department',
                to='departments.department'),
        ),
    ]
