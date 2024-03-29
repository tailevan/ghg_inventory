# Generated by Django 4.2.3 on 2023-12-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_emissionfactor_alter_officeoperationform_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeoperationform',
            name='commute',
            field=models.IntegerField(default=1500),
        ),
        migrations.AlterField(
            model_name='officeoperationform',
            name='electricity',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='officeoperationform',
            name='garbage',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='officeoperationform',
            name='paper',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='officeoperationform',
            name='water',
            field=models.IntegerField(default=1000),
        ),
    ]
