# Generated by Django 3.2.16 on 2022-12-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20221212_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
    ]
