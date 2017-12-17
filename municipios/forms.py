# -*- coding: utf-8 -*-
from django import forms

try:
    from widgets import SelectMunicipioWidget
except:
    # python 3.5.2 django1.9
    from municipios.widgets import SelectMunicipioWidget


class FormMunicipio(forms.Form):
    municipio = forms.IntegerField(label=u"UF - Município", widget=SelectMunicipioWidget, required=False)
