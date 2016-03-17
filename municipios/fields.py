# coding: utf-8
from django.db import models
from django.forms.models import ModelChoiceField
from widgets import SelectMunicipioWidget
from models import Municipio


class MunicipioChoiceField(ModelChoiceField):
    def __init__(self, *args, **kwargs):
        super(MunicipioChoiceField, self).__init__(*args, **kwargs)

        app_label = self.queryset.model._meta.app_label
        object_name = self.queryset.model._meta.object_name

        self.widget = SelectMunicipioWidget(app_label=app_label, object_name=object_name)

        extra_attrs = self.widget_attrs(self.widget)
        if extra_attrs:
            self.widget.attrs.update(extra_attrs)


class MunicipioForeignKey(models.ForeignKey):

    description = "Chave Estrangeira para um Municipio"

    def __init__(self, to=None, *args, **kwargs):
        if not to:
            to = Municipio
        super(MunicipioForeignKey, self).__init__(to, *args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MunicipioChoiceField}
        defaults.update(kwargs)
        return super(MunicipioForeignKey, self).formfield(**defaults)
