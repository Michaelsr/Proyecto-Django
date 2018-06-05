# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-06-05 03:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0004_usuario'),
        ('Venta', '0002_auto_20180523_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Producto', models.CharField(max_length=35)),
                ('Precio', models.PositiveSmallIntegerField()),
                ('FechaVenta', models.DateField()),
                ('Vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.Trabajador')),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
