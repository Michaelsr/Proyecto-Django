# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-06-14 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen', '0002_auto_20180512_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='PrecioCompra',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salida',
            name='PrecioCon',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Almacen.Ingreso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salida',
            name='PrecioVentaCaja',
            field=models.PositiveSmallIntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salida',
            name='PrecioVentaUnidad',
            field=models.PositiveSmallIntegerField(default=7),
            preserve_default=False,
        ),
    ]
