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


Dependências
============

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
  

Utilizando dados geográficos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
Se for utilizar GIS adicione a variável ``MUNICIPIOS_GEO``:


:: 
  
    MUNICIPIOS_GEO = True 

   
No settings.py, antes de rodar o `syncdb`.
Este parâmetro habilita os campos que armazenam dados Geográficos (GeoDjango).

Para carregar dados geográficos de todos os Municípios e UFs baixe o arquivo de fixture 
municipios_geo_900913.json.bz2_ (27.5 MB), e carregue a fixture com 

::
    
    python manage.py loaddata municipios_geo_900913.json.bz2

.. _municipios_geo_900913.json.bz2: https://github.com/downloads/znc-sistemas/django-municipios/municipios_geo_900913.json.bz2
    
    
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
1. Inclua o jquery no seu template, ou adicione ao media do seu Form.
2. form.media - o widget depende de codigo js para funcionar o ajax

::

    <script type="text/javascript" src="{{ STATIC_URL }}js/jquery.min.js"></script>

    {{ form.media }}

    {{ form }}


Template para o widget
~~~~~~~~~~~~~~~~~~~~~~  
A partir da versão 0.8.0 é possível customizar o template utilizado para apresentar o widget.
Os templates identificados pela aplicação são :

1. municipio_field.html
2. uf_field.html

e o nome da variável a ser substituída é ``{{wselect}}``

    ex.: de template para BootStrapTwitter

::

    <div class="control-group">
        <div class="controls"><label>Município</label> {{wselect}}  </div>
    </div>

adicione o HTML acima em um template dentro de por exemplo <app>/municipios/templates/municipios/municipio_field.html


URLs
~~~~
Adicionar as urls da aplicação no arquivo definido pelo ``ROOT_URLCONF`` do setings.py.

.. admonition:: Nota

   A partir da versão 1.4 do Django o prefixo da url pode ser qualquer um, nas versões 
   anteriores é necessário utilizar o prefixo "muncipios_app".

::

    (

    ...

    url(r'^municipios_app/', include('municipios.urls')),

    ...

    )

Arquivos Estáticos
~~~~~~~~~~~~~~~~~~

Para o funcionamento do widget de seleção de municípios em ambiente de produção é necessário utilizar o comando collectstatic_ do ``Static Files``.


.. _collectstatic: https://docs.djangoproject.com/en/1.4/ref/contrib/staticfiles/#collectstatic