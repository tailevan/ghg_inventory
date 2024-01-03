# Generated by Django 4.2.3 on 2023-12-29 05:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_officeoperationform_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmissionFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ef_electricity', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ef_water', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ef_paper', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ef_garbage', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ef_food', models.DecimalField(decimal_places=3, max_digits=5)),
                ('ef_commute', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.AlterField(
            model_name='officeoperationform',
            name='year',
            field=models.IntegerField(default=2023, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]