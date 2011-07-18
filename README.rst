==================================
Municípios Brasileiros para Django
==================================

Aplicação plugável Django com modelos e widgets para os Municípios Brasileiros


Instalando o django-municipios
==============================

    $ pip install django-municipios
    
ou
    
    $ easy_install django-municipios

ou baixar o código fonte do github e rodar "setup.py":

     $ git clone git://github.com/znc-sistemas/django-municipios.git
     $ cd django-municipios
     $ python setup.py install

DEPENDÊNCIAS
=============

 * jQuery (somente para utilizar widget de seleção de Municípios)  

Usando o django-municipios
==========================

SETTINGS
~~~~~~~~
adicione a aplicação no INSTALLED_APP no seu settings.py

::

    INSTALLED_APPS = (
        ...

        'municipios',

        ...

    )
  
    
Se for utilizar GIS adicione a variável MUNICIPIOS_GEO:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:: 
  
    MUNICIPIOS_GEO = True 

   
No settings.py, antes de rodar o `syncdb`.
Este parâmetro habilita os campos que armazenam dados Geográficos (GeoDjango) 
    
    
Utilizando o widget de Seleção de Municípios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

::

    from django import forms
    from municipios.widgets import SelectMunicipioWidget

    class FormEndereco(forms.Form):
        municipio = forms.IntegerField(label=u"UF - Município", widget=SelectMunicipioWidget)


View
~~~~

::

     def teste(request):
         form = FormEndereco()
         return render_to_response('endereco/teste.html', 
                {'form':form,}, context_instance = RequestContext(request))


Template
~~~~~~~~  
1. Inclua o jquery no seu template.
2. form.media - o widget depende de codigo js para funcionar o ajax

::

    <script type="text/javascript" src="{{ STATIC_URL }}js/jquery-1.5.2.min.js"></script>

    {{form.media}}

    {{form}}


URLs
~~~~
1. Adiciona o staticfiles.urls . O Widget depende de um arquivo javascript incluso no widget
2. url "municipios_app" - por enquanto é ncessário a utilização desta url para inclusão correta do template 

::

    (

    ...

    url(r'^municipios_app/', include('municipios.urls')),

    url(r'^teste/', 'endereco.views.teste', name='teste'),

    ...

    )

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
