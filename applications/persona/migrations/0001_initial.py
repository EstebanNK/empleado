# Generated by Django 3.1.4 on 2021-01-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'contador'), ('1', 'administrador'), ('2', 'economista'), ('3', 'otro')], max_length=50, verbose_name='Trab')),
            ],
        ),
    ]