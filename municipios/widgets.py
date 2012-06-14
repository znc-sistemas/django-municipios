# -*- coding: utf-8 -*-
from django.forms.widgets import Widget, TextInput, Select, MultiWidget, HiddenInput, Input
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from municipios.models import Municipio, UF

class SelectMunicipioWidget(Widget):
    """
    Widget to render a <select> with the UFs (Brazillian states)
    and a <select> with the actual Municipio depending on the state
    selected
    """
        
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        attrs = attrs or {}
        if attrs:
            self.attrs.update(attrs)
        
        output = []
        uf_val = ''
        uf_choices = [('','--')]+[(uf.pk,uf.uf) for uf in UF.objects.order_by('uf')]
        uf_select = Select(choices=uf_choices)
        municipio_select = Select(choices=(('','--'),))
        
        if value:
            try:
                municipio = Municipio.objects.get(pk=value)
                uf_val = municipio.uf.pk
                mun_choices = [(m.pk, m.nome) for m in Municipio.objects.filter(uf=uf_val).order_by('nome')]
                municipio_select = Select(choices=[('','- Selecione -')]+mun_choices)
            except Municipio.DoesNotExist:
                pass
        uf_attrs = self.attrs.copy()
        uf_attrs.update({"id":'%s_uf' % name, "onchange":"changeUF(this);"})
        select_html = uf_select.render('%s_uf' % name, uf_val, attrs=uf_attrs)
        required = False
        if 'class' in self.attrs:
            required = self.attrs['class'] == 'required'
        output.append(u'<div class="field"><label%s>UF</label><br />%s</div>' % (required and ' class="required"' or '', select_html))
        
        munic_attrs = self.attrs.copy()
        munic_attrs['style']="width:250px;"
        select_html = municipio_select.render(name, value, munic_attrs)
        output.append(u'<div class="field"><label%s>Município</label><br />%s</div>' % (required and ' class="required"' or '', select_html))
        return mark_safe(u'\n'.join(output))
    
    class Media:
        js = ( 'municipios/js/municipio.js',)

