# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pannol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('0', 'Funcional'), ('1', 'Defectuoso'), ('2', 'En reparación'), ('3', 'Ausente')], default='0', max_length=1)),
                ('serial', models.CharField(blank=True, max_length=100)),
                ('informacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pannol.InfoProducto')),
            ],
        ),
    ]
