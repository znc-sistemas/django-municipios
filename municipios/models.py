# -*- coding: utf-8 -*-
from django.conf import settings

MUNICIPIOS_GEO = getattr(settings,'MUNICIPIOS_GEO', False)

if MUNICIPIOS_GEO:
    from django.contrib.gis.db import models
else:
    from django.db import models

SRID = None
if MUNICIPIOS_GEO:
    SRID = getattr(settings,'MUNICIPIOS_SRID', 900913)
    
    
    
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
        objects = models.GeoManager()

    def __unicode__(self):
        return self.nome
    
         
class Municipio(models.Model):
    """
    Municípios do Brasil
    """
    id_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    nome_abreviado = models.CharField(max_length=150, blank=True, null=True)    
    uf = models.ForeignKey(UF)
    uf_sigla = models.CharField(max_length=2)
    if MUNICIPIOS_GEO: 
        sede = models.PointField(srid=SRID, null=True, blank=True)
        geom = models.MultiPolygonField(srid=SRID, null=True, blank=True)
        objects = models.GeoManager()
            
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.uf_sigla)
    
