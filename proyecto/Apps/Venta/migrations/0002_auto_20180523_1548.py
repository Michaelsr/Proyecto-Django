# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-23 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Producto', models.CharField(max_length=35)),
                ('Precio', models.CharField(max_length=35)),
            ],
        ),
        migrations.RemoveField(
            model_name='ventafactura',
            name='Vendedor',
        ),
        migrations.DeleteModel(
            name='VentaFactura',
        ),
    ]
