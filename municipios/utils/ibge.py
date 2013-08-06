# -*- coding: utf-8 -*-
from __future__ import print_function
from django.contrib.gis.gdal import DataSource, SpatialReference, CoordTransform, OGRGeometry, OGRGeomType
from django.contrib.gis.gdal.geometries import Polygon
from django.template.defaultfilters import slugify
from municipios.models import UF, Municipio, MUNICIPIOS_GEO, SRID
import sys

KEEP_LOWCASE = ('de', 'da', 'das', 'do', 'dos',)

UF_SIGLAS = (
    (11, 'RO'),
    (12, 'AC'),
    (13, 'AM'),
    (14, 'RR'),
    (15, 'PA'),
    (16, 'AP'),
    (17, 'TO'),
    (21, 'MA'),
    (22, 'PI'),
    (23, 'CE'),
    (24, 'RN'),
    (25, 'PB'),
    (26, 'PE'),
    (27, 'AL'),
    (28, 'SE'),
    (29, 'BA'),
    (31, 'MG'),
    (32, 'ES'),
    (33, 'RJ'),
    (35, 'SP'),
    (41, 'PR'),
    (42, 'SC'),
    (43, 'RS'),
    (50, 'MS'),
    (51, 'MT'),
    (52, 'GO'),
    (53, 'DF')
)

UF_SIGLAS_DICT = dict([(str(c), u) for c, u in UF_SIGLAS])

def capitalize_name(s):
    res = []
    for w in s.lower().split(' '):
        if w in KEEP_LOWCASE:
            res.append(w)
        else:
            res.append(w.capitalize())
    return u" ".join(res)


def convert_shapefile(shapefilename, srid=4674):
    """
    shapefilename: considera nomenclatura de shapefile do IBGE para determinar se é UF 
                   ou Municípios.
                   ex. 55UF2500GC_SIR.shp para UF e 55MU2500GC_SIR.shp para Municípios
    srid: 4674 (Projeção SIRGAS 2000)
    """
    # /home/nando/Desktop/IBGE/2010/55MU2500GC_SIR.shp
    ds = DataSource(shapefilename)

    is_uf = shapefilename.upper().find('UF') != -1

    transform_coord = None
    if srid != SRID:
        transform_coord = CoordTransform(SpatialReference(srid), SpatialReference(SRID))

    if is_uf:
        model = UF
    else:
        model = Municipio

    ct = 0
    for f in ds[0]:

        # 3D para 2D se necessário
        if f.geom.coord_dim != 2:
            f.geom.coord_dim = 2

        # converte para MultiPolygon se necessário
        if isinstance(f.geom, Polygon):
            g = OGRGeometry(OGRGeomType('MultiPolygon'))
            g.add(f.geom)
        else:
            g = f.geom

        # transforma coordenadas se necessário
        if transform_coord:
            g.transform(transform_coord)

        # força 2D
        g.coord_dim = 2
        kwargs = {}

        if is_uf:
            kwargs['nome'] = capitalize_name(unicode(f.get(CAMPO_NOME_UF),'latin1'))
            kwargs['geom'] = g.ewkt
            kwargs['id_ibge'] = f.get(CAMPO_GEOCODIGO_UF)
            kwargs['regiao'] = capitalize_name(unicode(f.get(CAMPO_REGIAO_UF), 'latin1'))
            kwargs['uf'] = UF_SIGLAS_DICT.get(kwargs['id_ibge'])
        else:
            kwargs['nome'] = capitalize_name(unicode(f.get(CAMPO_NOME_MU),'latin1'))
            kwargs['geom'] = g.ewkt
            kwargs['id_ibge'] = f.get(CAMPO_GEOCODIGO_MU)
            kwargs['uf'] = UF.objects.get(pk=f.get(CAMPO_GEOCODIGO_MU)[:2])
            kwargs['uf_sigla'] = kwargs['uf'].uf
            kwargs['nome_abreviado'] = slugify(kwargs['nome'])
            # tenta corrigir nomes duplicados, são em torno de 242 nomes repetidos
            # adicionando a sigla do estado no final
            if Municipio.objects.filter(nome_abreviado=kwargs['nome_abreviado']).count() > 0:
                kwargs['nome_abreviado'] = u'%s-%s' % (kwargs['nome_abreviado'], kwargs['uf_sigla'].lower())

        instance = model(**kwargs)
        instance.save()

        ct += 1

    print(ct, (is_uf and "Unidades Federativas criadas" or "Municipios criados"))
    
    
def update_sedes_municipais(shapefilename, srid=4618):
    # dados de um shapefile de 2001
    ds = DataSource(shapefilename)
    
    transform_coord = None
    if srid != SRID:
        transform_coord = CoordTransform(SpatialReference(srid), SpatialReference(SRID))

    ct = 0
    cta = 0
    for f in ds[0]:
        ct +=1
        cod = f.get('CODIGO')
        muns = Municipio.objects.extra(where=['CAST(id_ibge AS VARCHAR) ILIKE %s'], params=['%s%%' % cod])
        if muns:
            if len(muns) > 1:
                print("Mais de 1 municipio para", cod)
                for m in muns:
                    print(m.id_ibge, m)
            else:
                g = f.geom
                g.srs = SpatialReference(srid)
                g.srid = srid
                if transform_coord:
                    g.transform(transform_coord)
                print(g.ewkt)
                muns[0].sede = g.ewkt
                muns[0].save()
                cta += 1
        else:
            print(cod, "nao econtrado!")
    
    print("Atualizados", cta, "sedes")
    print("Total de", ct, "registros no shapefile")
        
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Informe o arquivo shapefile!")
    else:
        convert_shapefile(sys.argv[1])
