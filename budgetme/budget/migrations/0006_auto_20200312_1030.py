# Generated by Django 3.0.2 on 2020-03-12 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20200312_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='income',
            name='is_ongoing',
        ),
    ]
