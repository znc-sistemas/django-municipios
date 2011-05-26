from django.conf.urls.defaults import patterns, include, url

from views import municipios_ajx
urlpatterns = patterns('',
    url(r'^ajax/municipios/(?P<uf>\w\w)/$', municipios_ajx, name='ajax-municipios'),   
    url(r'^teste/', 'municipios.views.teste', name='munuf'),
    

)
