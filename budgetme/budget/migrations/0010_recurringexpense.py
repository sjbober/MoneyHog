# Generated by Django 3.0.2 on 2020-04-28 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0009_auto_20200427_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('day', models.IntegerField(verbose_name='Day of expense')),
                ('vendor', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='budget.Category')),
            ],
        ),
    ]