from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

from municipios.forms import FormMunicipio


def base_url_js(request):
    return HttpResponse(u"var __municipios_base_url__ = '%s';" % reverse('municipios-base-url'))


def municipios_ajax(request, uf, app_label, object_name):
    model_cls = apps.get_model(app_label, object_name)

    municipio_list = model_cls.objects.filter(Q(uf=uf)).order_by('nome')
    return render(
        request,
        "municipios/municipios_options.html",
        {"municipio_list": municipio_list},
    )


def teste(request):
    form = FormMunicipio(request.GET or None)
    return render(
        request,
        'municipios/teste.html',
        {'form': form},
    )
