# -*- coding: utf-8 -*-
from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError

from municipios.utils.ibge import convert_shapefile

class Command(BaseCommand):
    args = '<IBGE shapefile>'
    help = u'Importa shapefile do IBGE para os modelos UF e Municipio'
    
    def handle(self, *args, **options):
        if not args:
            raise CommandError('Arquivo Shapefile do IBGE não especificado!')
        print("Convertendo '%s':" % args[0])
        convert_shapefile(args[0])