# Generated by Django 3.1.4 on 2021-01-24 16:31

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_employeetimesheet_campus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetimesheet',
            name='checkin_image',
            field=models.ImageField(blank=True, null=True, upload_to=backend.models.upload_to_employee_attendance),
        ),
        migrations.AlterField(
            model_name='employeetimesheet',
            name='checkin_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeetimesheet',
            name='checkout_image',
            field=models.ImageField(blank=True, null=True, upload_to=backend.models.upload_to_employee_attendance),
        ),
        migrations.AlterField(
            model_name='employeetimesheet',
            name='checkout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]