from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from django.http import HttpResponse
from .models import Sites, Biblio, Staticmap, Mobiliers

from .forms import MobiliersUploadForm

# from django.views.decorators.http import require_POST
# from django.http import HttpResponseRedirect
# from django.views.generic.edit import FormView
# from .forms import FileFieldForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def home(request):
	context = {
	    'sites':Sites.objects.all()
	}
	return render(request, 'touim/home.html', context)


class SitesListView(ListView):
	model = Sites
	template_name = 'touim/home.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'sites'
	# ordering = ['-date_posted']
	paginate_by = 10


class SitesDetailView(DetailView):
	model = Sites
	mobiliers = Mobiliers.objects.all()
	biblios = Biblio.objects.all()


class SitesCreateView(LoginRequiredMixin, CreateView):
	model = Sites
	fields = ['id', 'sitename', 'descr', 'coordx', 'coordy', 'discovered']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class SitesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Sites
	fields = ['id', 'sitename', 'descr', 'coordx', 'coordy', 'discovered', 'site_logo', 'topo']

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
	template_name = 'touim/mobilier.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'mobiliers'
	# ordering = ['-date_posted']
	paginate_by = 4


def mobilier_create(request):
    if request.method == 'POST':
        m_form = MobiliersUploadForm(request.POST, request.FILES)
        if m_form.is_valid():
            instance = Mobiliers(mob_logo=request.FILES['mob_logo'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        m_form = MobiliersUploadForm()
    return render(request, 'touim/mobilier_create.html', {'m_form': m_form})


# def mobilier_create(request, site_id):
#     form = MobiliersForm(request.POST or None, request.FILES or None)
#     site = get_object_or_404(Sites, pk=site_id)
#     if form.is_valid():
#         sites_mobiliers = site.mobiliers_set.all()
#         for s in sites_mobiliers:
#             if s.mob_nom == form.cleaned_data.get("mob_nom"):
#                 context = {
#                     'site': site,
#                     'form': form,
#                     'error_message': 'You already added that mobilier',
#                 }
#                 return render(request, 'touim/mobilier_create.html', context)
#         mobilier = form.save(commit=False)
#         mobilier.site = site
#         mobilier.mob_logo = request.FILES['mob_logo']
#         file_type = mobilier.mob_logo.url.split('.')[-1]
#         file_type = file_type.lower()
#         if file_type not in IMAGE_FILE_TYPES:
#             context = {
#                 'site': site,
#                 'form': form,
#                 'error_message': 'Image file must be PNG, JPG or JPEG',
#             }
#             return render(request, 'touim/mobilier_create.html', context)

#         mobilier.save()
#         return render(request, 'touim/sites_detail.html', {'site': site})
#     context = {
#         'site': site,
#         'form': form,
#     }
#     return render(request, 'touim/mobilier_create.html', context)


def about(request):
	return render(request, 'touim/about.html', {'title':'About'})


def layers(request):
	return render(request, 'touim/layers.html')


def layers2(request):
	cartos = Staticmap.objects
	return render(request, 'touim/layers2.html', {'cartos':cartos})


def carto(request):
	cartos = Staticmap.objects.all()
	return render(request, 'touim/cartography.html', {'cartos':cartos})


def biblio(request):
	biblios = Biblio.objects.all()
	return render(request, 'touim/bibliography.html', {'biblios':biblios})


