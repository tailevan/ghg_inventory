# Generated by Django 4.2.3 on 2023-12-29 02:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeOperationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricity', models.IntegerField()),
                ('water', models.IntegerField()),
                ('paper', models.IntegerField()),
                ('garbage', models.IntegerField()),
                ('food', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('commute', models.IntegerField()),
            ],
        ),
    ]
