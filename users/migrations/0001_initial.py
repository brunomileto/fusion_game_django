# Generated by Django 3.0.8 on 2020-07-11 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture_url', models.CharField(default='something', max_length=240)),
                ('phone', models.CharField(default=None, max_length=120, null=True)),
                ('cpf', models.CharField(default=None, max_length=120, null=True, unique=True)),
                ('rg', models.CharField(default=None, max_length=120, null=True, unique=True)),
                ('birth_date', models.DateField(default=None, null=True)),
                ('wallet', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('psn_gametag', models.CharField(default=None, max_length=120, null=True)),
                ('xbox_gametag', models.CharField(default=None, max_length=120, null=True)),
                ('bank_name', models.CharField(default=None, max_length=120, null=True)),
                ('bank_account', models.CharField(default=None, max_length=120, null=True, unique=True)),
                ('bank_agency', models.CharField(default=None, max_length=120, null=True, unique=True)),
                ('user_status', models.CharField(default='available', max_length=120)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
