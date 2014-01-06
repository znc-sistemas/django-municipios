# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import FormMunicipio
from models import Municipio


def base_url_js(request):
    return HttpResponse(u"var __municipios_base_url__ = '%s';" % reverse('municipios-base-url'))


def municipios_ajax(request, uf):
    municipio_list = Municipio.objects.filter(uf=uf).order_by('nome')

    return render_to_response("municipios/municipios_options.html",
                              {"municipio_list": municipio_list},
                              context_instance=RequestContext(request))


def teste(request):
    form = FormMunicipio(request.GET or None)
    return render_to_response('municipios/teste.html',
                              {'form': form},
                              context_instance=RequestContext(request),)
