# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_ibge', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('nome_abreviado', models.CharField(max_length=150, null=True, blank=True)),
                ('uf_sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id_ibge', models.IntegerField(serialize=False, primary_key=True)),
                ('uf', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=20)),
                ('regiao', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(to='municipios.UF'),
        ),
    ]

    if settings.MUNICIPIOS_GEO:
        SRID = getattr(settings, 'MUNICIPIOS_SRID', 900913)
        import django.contrib.gis.db.models.fields
        operations.extend([
            migrations.AddField(
                model_name='municipio',
                name='geom',
                field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=SRID)
            ),
            migrations.AddField(
                model_name='municipio',
                name='sede',
                field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=SRID)
            ),
            migrations.AddField(
                model_name='uf',
                name='geom',
                field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=SRID)
            ),
        ])
