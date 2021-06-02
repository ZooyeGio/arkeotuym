from django import forms
from django.contrib.auth.models import User
from .models import Sites, Mobiliers
from django.utils.translation import gettext_lazy as _


class SiteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["descr"].widget = forms.Textarea()
        self.fields['descr'].widget.attrs.update({'class': 'narrow-select'})

    class Meta:
        model = Sites
        fields = '__all__'
        exclude = ['id_site', 'user', 'biblio']
        labels = {
            'sitename':_('Name of site'),
            'oper':_('Type of operation'),
            'descr': _('Description'),
            'site_img': _('Image'),
            'date': _('Dates'),
        }


class MobiliersCreateForm(forms.ModelForm):

    class Meta:
        model = Mobiliers
        fields = ['mob_nom', 'mob_img']
        labels = {
            'mob_nom':_('Name'),
            'mob_img':_('Image')
        }
        help_texts = {
            'mob_nom': _('Some useful help text.'),
        }
