# Generated by Django 3.0.2 on 2020-04-29 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0011_remove_recurringexpense_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurringexpense',
            name='vendor',
        ),
    ]
