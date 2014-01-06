# -*- coding: utf-8 -*-
from django import forms

from widgets import SelectMunicipioWidget


class FormMunicipio(forms.Form):
    municipio = forms.IntegerField(label=u"UF - Município", widget=SelectMunicipioWidget, required=False)
