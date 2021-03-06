# Generated by Django 3.0.6 on 2020-05-19 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbook', '0009_auto_20200518_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='published_company',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='published_year',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex='(19[0-9]{2}|20[0-9]{2})')]),
        ),
    ]
