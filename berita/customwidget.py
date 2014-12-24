from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy
from django.forms.widgets import ClearableFileInput, CheckboxInput, FileInput

class AdvancedFileInput(ClearableFileInput):

    def __init__(self, *args, **kwargs):
        self.url_length = kwargs.pop('url_length',30)
        self.preview = kwargs.pop('preview',True)
        self.image_width = kwargs.pop('image_width',200)
        super(AdvancedFileInput, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': 'File saat ini',
            'input_text': 'Ganti File',
            'clear_template': '',
            'clear_checkbox_label': 'Hapus?',
        }
        template = '%(input)s'
        substitutions['input'] = super(ClearableFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = (u'<a href="{0}">{1}</a><br><br>'.format
                    (escape(value.url),'...'+escape(force_unicode(value))[-self.url_length:],
                     self.image_width))
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)

class AdvancedClearableFileInput(ClearableFileInput):

    def __init__(self, *args, **kwargs):

        self.url_length = kwargs.pop('url_length',30)
        self.preview = kwargs.pop('preview',True)
        self.image_width = kwargs.pop('image_width',150)
        super(AdvancedClearableFileInput, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None,):

        substitutions = {
            'initial_text': 'Gambar saat ini',
            'input_text': 'Ganti Gambar',
            'clear_template': '',
            'clear_checkbox_label': 'Hapus?',
        }
        template = u'%(input)s'

        substitutions['input'] = super(ClearableFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):

            template = self.template_with_initial
            if self.preview:
                substitutions['initial'] = (u'<a href="{0}">{1}</a><br>\
                <a href="{0}" target="_blank"><img src="{0}" width="{2}"></a><br>'.format
                    (escape(value.url),'...'+escape(force_unicode(value))[-self.url_length:],
                     self.image_width))
            else:
                substitutions['initial'] = (u'<a href="{0}">{1}</a>'.format
                    (escape(value.url),'...'+escape(force_unicode(value))[-self.url_length:]))
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)
