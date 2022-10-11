# Generated by Django 2.0.3 on 2018-03-08 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0003_remove_identitytype_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='livestock.Breed', verbose_name='breed'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='herd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.Herd', verbose_name='herd'),
        ),
    ]