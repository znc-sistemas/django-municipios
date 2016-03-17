# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.apps import apps

from forms import FormMunicipio


def base_url_js(request):
    return HttpResponse(u"var __municipios_base_url__ = '%s';" % reverse('municipios-base-url'))


def municipios_ajax(request, uf, app_label, object_name):
    model_cls = apps.get_model(app_label, object_name)

    municipio_list = model_cls.objects.filter(Q(uf=uf)).order_by('nome')
    return render_to_response("municipios/municipios_options.html",
                              {"municipio_list": municipio_list},
                              context_instance=RequestContext(request))


def teste(request):
    form = FormMunicipio(request.GET or None)
    return render_to_response('municipios/teste.html',
                              {'form': form},
                              context_instance=RequestContext(request),)
