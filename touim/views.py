from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Sites, Staticmap, Mobiliers, Images
from .forms import SiteForm, MobiliersCreateForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def home(request):
    sites = Sites.objects.filter()
    mobilier_results = Mobiliers.objects.all()
    query = request.GET.get("q")
    if query:
        sites = sites.filter(
            Q(sitename__icontains=query) |
            Q(oper__icontains=query)
        ).distinct()
        mobilier_results = mobilier_results.filter(
            Q(mob_nom__icontains=query)
        ).distinct()
        return render(request, 'touim/home.html', {
            'sites': sites,
            'mobiliers': mobilier_results,
        })
    else:
        paginator = Paginator(sites, 10)
        page = request.GET.get('page')
        sites = paginator.get_page(page)
        return render(request, 'touim/home.html', {'sites': sites})


class SitesDetailView(DetailView):
    model = Sites
    mobiliers = Mobiliers.objects.all()


def site_create(request):
    s_form = SiteForm(request.POST or None, request.FILES or None)
    if s_form.is_valid():
        site = s_form.save(commit=False)
        site.user = request.user
        site.site_img = request.FILES['site_img']
        # site.topo = request.FILES['topo']
        file_type = site.site_img.url.split('.')[-1]
        # file_typetopo = site.topo.url.split('.')[-1]
        file_type = file_type.lower()
        # file_typetopo = file_typetopo.lower()
        # if file_type and file_typetopo not in IMAGE_FILE_TYPES:
        #     context = {
        #     'site': site,
        #     's_form': s_form,
        #     'error_message': 'Image file must be PNG, JPG, or JPEG',
        #     }
        #     return render(request, 'touim/sites_create.html', context)
        if file_type not in IMAGE_FILE_TYPES:
            context = {
            'site': site,
            's_form': s_form,
            'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'touim/sites_create.html', context)
        site.save()
        object = site
        return render(request, 'touim/sites_detail.html', {'object':object})
    context = {"s_form": s_form,}
    return render(request, 'touim/site_create.html', context)


# fonctionne mais ne modifie pas les images:
class SitesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sites
    fields = '__all__'
    exclude = ['user', 'biblio']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        site = self.get_object()
        if self.request.user == site.user:
            return True
        return False


class SitesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sites
    success_url = '/'

    def test_func(self):
        site = self.get_object()
        if self.request.user == site.user:
            return True
        return False


class MobiliersListView(ListView):
    model = Mobiliers
    template_name = 'touim/mobilier.html'  # pattern: <app>/<model>_<viewtype>.html
    context_object_name = 'mobiliers'
    ordering = ['id']
    paginate_by = 4


def mobilier_create(request, site_id):
    m_form = MobiliersCreateForm(request.POST or None, request.FILES or None)
    site = get_object_or_404(Sites, pk=site_id)
    if m_form.is_valid():
        sites_mobiliers = site.mobiliers_set.all()
        for s in sites_mobiliers:
            if s.mob_nom == m_form.cleaned_data.get("mob_nom"):
                context = {
                    'site':site,
                    'm_form':m_form,
                    'error_message':'You already added that object'
                }
                return render(request, 'touim/mobilier_create.html', context)
        mobilier = m_form.save(commit=False)
        mobilier.site = site
        mobilier.mob_img = request.FILES['mob_img']
        file_type = mobilier.mob_img.url.split('.')[-1]
        file_type = file_type.lower()
        object = site
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'site':'site',
                'm_form':'m_form',
                'error_message': 'Image file must be PNG, JPG or JPEG'
            }
            return render(request, 'touim/mobilier_create.html', context)

        mobilier.save()
        return render(request, 'touim/sites_detail.html', {'object':object})
    context = {
        'site':site,
        'm_form':m_form,
    }
    return render(request, 'touim/mobilier_create.html', context)


class MobiliersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mobiliers
    success_url = '/'
    sites = Sites.objects.all()

    def test_func(self):
        mobilier = self.get_object()
        if self.request.user == mobilier.user:
            return True
        return False


def about(request):
    images = Images.objects.all()
    return render(request, 'touim/about.html', {'title':'About', 'images':images})


def layers(request):
    return render(request, 'touim/layers.html')


def layers2(request):
    sites = Sites.objects.all()
    return render(request, 'touim/layers2.html', {'sites':sites})


def carto(request):
    cartos = Staticmap.objects.all()
    return render(request, 'touim/cartography.html', {'cartos':cartos})
