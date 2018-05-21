# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-13 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaSalida', models.DateTimeField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Almacen.Producto')),
            ],
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='FechaIngreso',
            field=models.DateTimeField(),
        ),
    ]