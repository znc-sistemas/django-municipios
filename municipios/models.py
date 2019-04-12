# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

MUNICIPIOS_GEO = getattr(settings, 'MUNICIPIOS_GEO', False)

if MUNICIPIOS_GEO:
    from django.contrib.gis.db import models
else:
    from django.db import models

SRID = None
if MUNICIPIOS_GEO:
    SRID = getattr(settings, 'MUNICIPIOS_SRID', 900913)


@python_2_unicode_compatible
class UF(models.Model):
    """
    Unidades Federativas (Estados) do Brasil
    """
    id_ibge = models.IntegerField(primary_key=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=20)
    regiao = models.CharField(max_length=20)
    if MUNICIPIOS_GEO:
        geom = models.MultiPolygonField(srid=SRID, null=True, blank=True)

    def __str__(self):
        return self.nome


@python_2_unicode_compatible
class Municipio(models.Model):
    """
    Municípios do Brasil
    """
    id_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    nome_abreviado = models.CharField(max_length=150, blank=True, null=True)
    uf = models.ForeignKey(UF, models.PROTECT)
    uf_sigla = models.CharField(max_length=2)
    if MUNICIPIOS_GEO:
        sede = models.PointField(srid=SRID, null=True, blank=True)
        geom = models.MultiPolygonField(srid=SRID, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.nome, self.uf_sigla)
