# Generated by Django 3.2.16 on 2022-12-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0005_auto_20221212_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='region',
        ),
    ]