# Generated by Django 5.0.4 on 2024-07-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_owner_car_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
