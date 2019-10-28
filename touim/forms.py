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
            'oper':_('Тип архео операции'),
            'sitename':_('Название стоянки'),
            'infor':_('Информация'),
            'descr': _('Описание'),
            'site_logo': _('Изображение'),
            'periode': _('Датировка'),
            'coordx': _('Координаты по оси X'),
            'coordy': _('Координаты по оси Y'),
            'paleol': _('Палеолит'),
            'discovered': _('Дата открытия'),
            'bronze': _('Бронзовый век'),
            'iron': _('Железный век'),
            'mesol': _('Мезолит'),
            'middle_age': _('Средневековье'),
            'neol1': _('Ранний неолит'),
            'neol2': _('Средний неолит'),
            'neol3': _('Подзний неолит'),
            'passport': _('Номер паспорта'),
            'topo': _('Топо план'),
        }


# class home(forms.ModelForm):

#     class Meta:
#         model = Sites
#         fields = '__all__'
#         paginate_by = 2


class MobiliersCreateForm(forms.ModelForm):

    class Meta:
        model = Mobiliers
        fields = ['mob_nom', 'mob_logo']
        labels = {
            'mob_nom':_('Название'),
            'mob_logo':_('Изображение')
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
            # 'id_biblio':_('N°'),
            'titre':_('Название'),
            'autor':_('Автор'),
            'year':_('Год'),
            'tip':_('Тип'),
            'coll':_('Коллекция'),
            'edition':_('Издательство'),
            'pages':_('Страницы'),
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


# class BiblioCreateForm(forms.ModelForm):
#     class Meta:
#         model = Biblio
#         fields = ['id_biblio', 'titre', 'autor', 'year', 'site']
