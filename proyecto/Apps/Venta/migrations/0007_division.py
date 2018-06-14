# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-06-14 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venta', '0006_auto_20180614_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('num2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('resultado', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
