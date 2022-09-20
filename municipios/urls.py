from django.urls import path, re_path

import municipios.views as mviews

urlpatterns = (
    path('', mviews.base_url_js, name='municipios-base-url'),
    path('base_url.js', mviews.base_url_js, name='municipios-base-url-js'),
    re_path('^ajax/municipios/(?P<uf>\w\w)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', mviews.municipios_ajax, name='municipios-ajax'),
    path('teste/', mviews.teste, name='municipios-teste'),
)
