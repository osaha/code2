# Generated by Django 3.0.6 on 2020-05-18 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbook', '0008_auto_20200518_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookrequest',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='bookrequest',
            old_name='student_id',
            new_name='student',
        ),
    ]