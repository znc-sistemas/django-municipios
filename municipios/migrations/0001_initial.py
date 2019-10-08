# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.db.models.deletion

from django.db import models, migrations

from django.conf import settings
MUNICIPIOS_GEO = getattr(settings, 'MUNICIPIOS_GEO', False)
if MUNICIPIOS_GEO:
    from django.contrib.gis.db import models as models_geo


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
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='municipios.UF'),
        ),
    ]

    if MUNICIPIOS_GEO:
        SIRGAS_2000 = 4674
        MUNICIPIOS_SRID = getattr(settings, 'MUNICIPIOS_SRID', SIRGAS_2000)

        operations += [
            migrations.AddField(
                model_name='municipio',
                name='geom',
                field=models_geo.fields.MultiPolygonField(blank=True, null=True, srid=MUNICIPIOS_SRID),
            ),
            migrations.AddField(
                model_name='municipio',
                name='sede',
                field=models_geo.fields.PointField(blank=True, null=True, srid=MUNICIPIOS_SRID),
            ),
            migrations.AddField(
                model_name='uf',
                name='geom',
                field=models_geo.fields.MultiPolygonField(blank=True, null=True, srid=MUNICIPIOS_SRID),
            ),
        ]
