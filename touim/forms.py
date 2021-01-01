from django import forms
from django.contrib.auth.models import User
from .models import Sites, Mobiliers, Biblio
from django.utils.translation import gettext_lazy as _


class SiteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["infor"].widget = forms.Textarea()
        self.fields["descr"].widget = forms.Textarea()
        self.fields['infor'].widget.attrs.update({'class': 'narrow-select'})
        self.fields['descr'].widget.attrs.update({'class': 'narrow-select'})

    class Meta:
        model = Sites
        fields = '__all__'
        exclude = ['user', 'biblio']
        labels = {
            'oper':_('Type of operation'),
            'sitename':_('Name of site'),
            'infor':_('About'),
            'descr': _('Description'),
            'site_logo': _('Image'),
            'periode': _('Dates'),
            'coordx': _('coordinates X'),
            'coordy': _('coordinates Y'),
            'paleol': _('What'),
            'discovered': _('Discovered in'),
            'bronze': _('Bronze age'),
            'iron': _('Iron age'),
            'mesol': _('Mesolithic age'),
            'middle_age': _('Middle age'),
            'neol1': _('Early neolithic'),
            'neol2': _('Middle neolithic'),
            'neol3': _('Late neolithic неолит'),
            'passport': _('Document numer'),
            'topo': _('Plans topographic'),
        }


class MobiliersCreateForm(forms.ModelForm):

    class Meta:
        model = Mobiliers
        fields = ['mob_nom', 'mob_logo']
        labels = {
            'mob_nom':_('Name'),
            'mob_logo':_('Image')
        }
        help_texts = {
            'mob_nom': _('Some useful help text.'),
        }


# this class BiblioCreateForm is from https://stackoverflow.com/questions/49932426/save-many-to-many-field-django-forms
class BiblioCreateForm(forms.ModelForm):
    class Meta:
        model = Biblio
        fields = '__all__'
        labels = {
            'titre':_('Title'),
            'autor':_('Author'),
            'year':_('Year'),
            'tip':_('Type'),
            'coll':_('Collection'),
            'edition':_('Edition'),
            'pages':_('Pages'),
        }

    sites = forms.ModelMultipleChoiceField(queryset=Sites.objects.all())

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['sites'] = [t.pk for t in 
                kwargs['instance'].sites_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)

        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            instance.sites_set.clear()
            for site in self.cleaned_data['sites']:
                instance.sites_set.add(site)

        self.save_m2m = save_m2m
        
        instance.save()
        self.save_m2m()

        return instance

