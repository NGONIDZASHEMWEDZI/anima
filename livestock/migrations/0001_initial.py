# Generated by Django 2.0.3 on 2018-03-07 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gears', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('identifier', models.CharField(max_length=100, verbose_name='identifier')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='date of birth (AD)')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=10, verbose_name='gender')),
                ('is_pregnant', models.BooleanField(default=False, verbose_name='is pregnant')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='due date')),
                ('lactation', models.CharField(choices=[('Never', 'Never'), ('Lactating', 'Lactating'), ('Stopped', 'Stopped')], default='Never', max_length=20, verbose_name='lactation')),
                ('milk_day', models.FloatField(blank=True, null=True, verbose_name='milk per day (in litres)')),
                ('is_sick', models.BooleanField(default=False, verbose_name='is sick')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='weight')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('description', models.TextField(verbose_name='description')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='livestock.Animal')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalEventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalSickness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('is_recovered', models.BooleanField(default=False, verbose_name='is recovered')),
                ('recovered_on', models.DateField(blank=True, null=True, verbose_name='recovered on')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.Animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalTxn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('amount', models.FloatField()),
                ('remarks', models.CharField(blank=True, max_length=200)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.Animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('breeding_ages', models.CharField(blank=True, max_length=200, verbose_name='breeding ages')),
                ('animal_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livestock.AnimalType', verbose_name='animal type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Herd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdentityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=100)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.Animal')),
                ('txn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.AnimalTxn')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SicknessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TxnType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField()),
                ('name', models.CharField(max_length=200)),
                ('is_expense', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='txntype',
            unique_together={('name', 'is_expense')},
        ),
        migrations.AddField(
            model_name='medicine',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.MedicineType'),
        ),
        migrations.AddField(
            model_name='animaltxn',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livestock.TxnType'),
        ),
        migrations.AddField(
            model_name='animalevent',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='livestock.AnimalEventType'),
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='livestock.Breed', verbose_name='breed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gears.Farm', verbose_name='farm'),
        ),
        migrations.AddField(
            model_name='animal',
            name='herd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.Herd', verbose_name='herd'),
        ),
        migrations.AddField(
            model_name='animal',
            name='identity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.IdentityType', verbose_name='identity type'),
        ),
        migrations.AddField(
            model_name='animal',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='livestock.Animal', verbose_name='parent'),
        ),
        migrations.AlterUniqueTogether(
            name='animal',
            unique_together={('farm', 'identity_type', 'identifier')},
        ),
    ]
