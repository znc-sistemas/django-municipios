# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Municipio
from forms import FormMunicipio


def municipios_ajx(request, uf):
    municipio_list = Municipio.objects.filter(uf=uf).order_by('nome')

    return render_to_response("municipios/municipios_options.html",
                              {"municipio_list": municipio_list},
                              context_instance=RequestContext(request))
def teste(request):
    form = FormMunicipio()
    return render_to_response('municipios/teste.html',
                              {'form':form,},
                               context_instance=RequestContext(request),)
