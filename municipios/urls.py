try:
    from django.conf.urls import url
except:
    from django.conf.urls.defaults import url

import municipios.views as mviews

urlpatterns = (
    url(r'^$', mviews.base_url_js, name='municipios-base-url'),
    url(r'^base_url.js$', mviews.base_url_js, name='municipios-base-url-js'),
    url(r'^ajax/municipios/(?P<uf>\w\w)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', mviews.municipios_ajax, name='municipios-ajax'),
    url(r'^teste/', mviews.teste, name='municipios-teste'),
)
