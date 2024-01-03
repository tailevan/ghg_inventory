# Generated by Django 4.2.3 on 2024-01-01 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_officeoperationform_commute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeoperationform',
            name='year',
            field=models.IntegerField(default=2024, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]