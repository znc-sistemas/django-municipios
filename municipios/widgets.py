# -*- coding: utf-8 -*-
from django.forms.widgets import Select, Widget

from django.template.loader import get_template

from django.utils.safestring import mark_safe

from django.apps import apps

try:
    from django.core.urlresolvers import reverse_lazy
    HAS_REVERSE_LAZY = True
except ImportError:
    HAS_REVERSE_LAZY = False


class SelectMunicipioWidget(Widget):
    """
    Widget to render a <select> with the UFs (Brazillian states)
    and a <select> with the actual Municipio depending on the state
    selected
    """
    def __init__(self, *args, **kwargs):
        self.app_label = kwargs.pop('app_label', 'municipios')
        self.object_name = kwargs.pop('object_name', 'Municipio')
        self.mun_cls = apps.get_model(self.app_label, self.object_name)
        super(SelectMunicipioWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        attrs = attrs or {}
        if attrs:
            self.attrs.update(attrs)

        output = []
        uf_val = ''
        uf_choices = [('', '--')] + list(self.mun_cls.objects.values_list('uf__id_ibge', 'uf_sigla').distinct().order_by('uf_sigla'))
        uf_select = Select(choices=uf_choices)
        municipio_select = Select(choices=(('', '--'),))

        if value:
            try:
                municipio = self.mun_cls.objects.get(pk=value)
                uf_val = municipio.uf.pk
                mun_choices = [(m.pk, m.nome) for m in self.mun_cls.objects.filter(uf=uf_val).order_by('nome')]
                municipio_select = Select(choices=[('', '- Selecione -')] + mun_choices)
            except self.mun_cls.DoesNotExist:
                pass
        uf_attrs = self.attrs.copy()
        uf_attrs.update(
            {
                "id": '%s_uf' % name,
                "onchange": "changeUF(this);",
                "data-app_label": self.app_label,
                "data-object_name": self.object_name,
            }
        )
        select_html = uf_select.render('%s_uf' % name, uf_val, attrs=uf_attrs)
        required = False
        if 'class' in self.attrs:
            required = self.attrs['class']
        # output.append(u'<div class="field"><label%s>UF</label><br />%s</div>' % (required and ' class="required"' or '', select_html))
        template_uf = get_template('municipios/uf_field.html')
        context_uf = {'label_class': required, 'wselect': select_html}
        output.append(template_uf.render(context_uf))

        munic_attrs = self.attrs.copy()
        munic_attrs['style'] = "width:250px;"
        select_html = municipio_select.render(name, value, munic_attrs)
        # output.append(u'<div class="field"><label%s>Município</label><br />%s</div>' % (required and ' class="required"' or '', select_html))
        template_mun = get_template('municipios/municipio_field.html')
        context_mun = {'label_class': required, 'wselect': select_html}
        output.append(template_mun.render(context_mun))

        return mark_safe(u'\n'.join(output))

    class Media:
        if HAS_REVERSE_LAZY:
            base_url_js = reverse_lazy('municipios-base-url-js')
        else:
            base_url_js = '/municipios_app/base_url.js'
        js = (base_url_js, 'municipios/js/municipio.js',)
