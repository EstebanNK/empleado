# Generated by Django 3.1.4 on 2021-01-06 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
        ('persona', '0002_auto_20210105_2348'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleados',
            new_name='Empleado',
        ),
    ]