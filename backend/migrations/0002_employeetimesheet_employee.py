# Generated by Django 3.1.3 on 2020-11-29 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeetimesheet',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='backend.employee'),
            preserve_default=False,
        ),
    ]