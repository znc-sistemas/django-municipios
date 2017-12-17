from django import VERSION

# django 1.9 or >
um_nove_ou_maior = all([VERSION[0] == 1, VERSION[1] >= 9])

try:
    from django.conf.urls import patterns, url
except:
    from django.conf.urls.defaults import url

if um_nove_ou_maior:
    # não compativel com django 2.0 
    from municipios.views import (
        base_url_js,
        municipios_ajax,
        teste,
        )
    urlpatterns = [
        url(r'^$', base_url_js, name='municipios-base-url'),
        url(r'^base_url.js$', base_url_js, name='municipios-base-url-js'),
        url(r'^ajax/municipios/(?P<uf>\w\w)/$', municipios_ajax, name='municipios-ajax'),
        url(r'^teste/', teste, name='municipios-teste'),
    ]
else:
    # is deprecated and will be removed in Django 1.10
    urlpatterns = patterns(
        'municipios.views',
        url(r'^$', 'base_url_js', name='municipios-base-url'),
        url(r'^base_url.js$', 'base_url_js', name='municipios-base-url-js'),
        url(r'^ajax/municipios/(?P<uf>\w\w)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', 'municipios_ajax', name='municipios-ajax'),
        url(r'^teste/', 'teste', name='municipios-teste'),
    )
