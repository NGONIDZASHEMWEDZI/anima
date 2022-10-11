# Generated by Django 2.0.3 on 2018-03-10 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livestock', '0007_auto_20180310_1209'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.Animal', verbose_name='animal')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_products', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('about', models.TextField(verbose_name='about')),
                ('mobile', models.CharField(max_length=10, verbose_name='mobile number')),
                ('status', models.CharField(choices=[('Pending', 'Pending verification'), ('Verified', 'Verified'), ('Unverified', 'Unverified'), ('Banned', 'Banned'), ('Archived', 'Archived')], db_index=True, default='Pending', max_length=20, verbose_name='status')),
                ('checker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_sellers', to=settings.AUTH_USER_MODEL, verbose_name='profile checker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='market.Seller', verbose_name='seller'),
        ),
    ]