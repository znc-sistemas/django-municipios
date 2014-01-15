try:
    from django.conf.urls import patterns, url
except:
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'municipios.views',
    url(r'^$', 'base_url_js', name='municipios-base-url'),
    url(r'^base_url.js$', 'base_url_js', name='municipios-base-url-js'),
    url(r'^ajax/municipios/(?P<uf>\w\w)/$', 'municipios_ajax', name='municipios-ajax'),
    url(r'^teste/', 'teste', name='municipios-teste'),
)
