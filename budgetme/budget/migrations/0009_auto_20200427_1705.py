# Generated by Django 3.0.2 on 2020-04-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_auto_20200410_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]