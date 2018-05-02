# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-31 13:53
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20180331_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='crt_bat',
        ),
        migrations.RemoveField(
            model_name='player',
            name='crt_lake',
        ),
        migrations.RemoveField(
            model_name='player',
            name='crt_widget',
        ),
        migrations.AddField(
            model_name='player',
            name='avrisk',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='¿Apostarías S/.10 si existe un 50% de probabilidad de que ganes S/.5 más pero 50% de probabilidad de que pierdas S/. 5?'),
        ),
        migrations.AddField(
            model_name='player',
            name='corrup',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='¿Crees que existe corrupción en el Estado?'),
        ),
        migrations.AddField(
            model_name='player',
            name='malg',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='¿Crees que el Estado malgasta el dinero que recibe de los contribuyentes?'),
        ),
        migrations.AddField(
            model_name='player',
            name='tasa1',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='¿Es justificable que se aumente la tasa de impuestos si el Estado promete invertir el dinero en más obras para la población?'),
        ),
        migrations.AddField(
            model_name='player',
            name='tasa2',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='De acuerdo con la pregunta anterior, ¿Estarías dispuesto a contribuir con mayores impuestos a pesar de que las obras y políticas del Estado no te beneficien directamente?'),
        ),
        migrations.AddField(
            model_name='player',
            name='tax1',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='¿Es justificable pagar menores impuestos al Estado?'),
        ),
        migrations.AddField(
            model_name='player',
            name='tax2',
            field=otree.db.models.PositiveIntegerField(choices=[('Sí', 'Sí'), ('No', 'No')], null=True, verbose_name='¿Es justificable pagar menores impuestos al Estado, sabiendo que la probabilidad de ser atrapado es mínima?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='field',
            field=otree.db.models.StringField(choices=[('Economía', 'Economía'), ('Psicología', 'Psicología'), ('Derecho', 'Derecho'), ('Ingeniería', 'Ingeniería'), ('Gestión y Alta Dirección', 'Gestión y Alta Dirección'), ('Arquitectura', 'Arquitectura'), ('Sociología', 'Sociología'), ('Ciencias políticas', 'Ciencias políticas'), ('Antropología', 'Antropología'), ('C. Comunicación', 'C. Comunicación'), ('Humanidades', 'Humanidades'), ('Otra', 'Otra')], max_length=10000, null=True, verbose_name='¿Qué carrera estudias?'),
        ),
    ]