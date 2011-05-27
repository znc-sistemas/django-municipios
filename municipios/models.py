# -*- coding: utf-8 -*-

from django.conf import settings
GEO_MUNICIPIOS = getattr(settings,'GEO_MUNICIPIOS', False)

if GEO_MUNICIPIOS:
    from django.contrib.gis.db import models
else:
    from django.db import models

if GEO_MUNICIPIOS:
    SRID = getattr(settings,'SRID', '929102')
    
class UF(models.Model):
    id_ibge = models.IntegerField(primary_key=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=20)
    regiao = models.CharField(max_length=20)
    if GEO_MUNICIPIOS : the_geom = models.MultiPolygonField(srid=SRID)
    class Meta:
        db_table = u'uf'   

         
class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_ibge = models.CharField(unique=True, max_length=16)
    nome = models.CharField(max_length=150)
    nome_abreviado = models.CharField(max_length=15, blank=True, null=True)
    
    uf = models.ForeignKey(UF)
    uf_sigla = models.CharField(max_length=2)

    if GEO_MUNICIPIOS: the_geom = models.MultiPolygonField(srid=SRID)

    class Meta:
        db_table = u'municipio'
        
    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.uf)
    
