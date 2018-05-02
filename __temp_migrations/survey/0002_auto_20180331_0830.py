# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-31 13:30
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='field',
            field=otree.db.models.StringField(choices=[('Economía', 'Economía'), ('Psicología', 'Psicología')], max_length=10000, null=True, verbose_name='¿Qué carrera estudias?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=otree.db.models.PositiveIntegerField(null=True, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=otree.db.models.StringField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10000, null=True, verbose_name='Sexo'),
        ),
    ]