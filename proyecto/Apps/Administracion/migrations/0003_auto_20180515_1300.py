# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-15 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0002_auto_20180514_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Correo',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]