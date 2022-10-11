# Generated by Django 2.0.3 on 2018-03-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0008_auto_20180310_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='net_expense',
            field=models.PositiveIntegerField(default=0, verbose_name='net expense'),
        ),
        migrations.AddField(
            model_name='animal',
            name='net_income',
            field=models.PositiveIntegerField(default=0, verbose_name='net income'),
        ),
    ]