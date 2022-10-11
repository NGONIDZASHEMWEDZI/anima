# Generated by Django 2.0.3 on 2018-03-10 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livestock', '0005_auto_20180310_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaltxn',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_transactions', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]