# Generated by Django 3.0.8 on 2020-07-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20200726_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
