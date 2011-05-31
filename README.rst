==================================
Municípios Brasileiros para Django
==================================

Aplicação plugável Django com modelos e widgets para os Municípios Brasileiros


Instalando o django-municipios
==============================

    pip install django-muinicipios
    easy_install django-municipios

ou a baixar o código fonte do  github and run "setup.py::

     $ git clone git://github.com/znc-sistemas/django-municipios.git
     $ cd django-municipios
     $ python setup.py install

DEPENDENCIAS
=============

 * jQUery  

Usando o django-municipios
==========================

SETTINGS
~~~~~~~~
adicione a aplicação no INSTALLED_APP no seu settings.py
    INSTALLED_APPS = (
        ...

        'municipios',

        ...

    )  
    
Se for utilizar GIS adicione a variável GEO_MUNICIPIOS::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    GEO_MUNICIPIOS = True 

no "forms.py"
~~~~~~~~~~~~~ 
    from django import forms
    from municipios.widgets import SelectMunicipioWidget

    class FormEndereco(forms.Form):
        municipio = forms.IntegerField(label=u"UF - Municipio", widget=SelectMunicipioWidget, required=False)


View
~~~~

     def teste(request):
         form = FormEndereco()
         return render_to_response('endereco/teste.html', 
                {'form':form,}, context_instance = RequestContext(request))


Template
~~~~~~~~  
1. inclua o jquery no seu template.
2. form.media - o widget depende de codigo js para funcionar o ajax

    <script type="text/javascript" src="{{ STATIC_URL }}js/jquery-1.5.2.min.js"></script>

    {{form.media}}

    {{form}}

URLs
~~~~
1. Adiciona o staticfiles.urls . O WIDGET depende de um arquivo javascript incluso no widget
2. url "municipios_app" - por enquanto é ncessário a utilização desta url para inclusão correta do template 

    (

    ...

    url(r'^municipios_app/', include('municipios.urls')),

    url(r'^teste/', 'endereco.views.teste', name='teste'),

    ...

    )

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()