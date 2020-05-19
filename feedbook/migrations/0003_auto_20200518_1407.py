# Generated by Django 3.0.6 on 2020-05-18 05:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbook', '0002_auto_20200518_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='published_year',
            field=models.CharField(default='1900', max_length=4, validators=[django.core.validators.RegexValidator(regex='(19[0-9]{2}|20[0-9]{2})')]),
        ),
    ]