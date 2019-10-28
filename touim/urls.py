from django.urls import path
from .views import (
    # SitesListView, 
    SitesDetailView, 
    # SitesCreateView,
    SitesUpdateView,
    SitesDeleteView,
    MobiliersListView,
    MobiliersDeleteView
    )
from . import views

from django.conf import settings
from django.conf.urls.static import static

# from users import views as user_views
# from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # path('', SitesListView.as_view(), name='touim-home'),  # without search
    path('', views.home, name='touim-home'),  #for search
    path('site/<int:pk>/', SitesDetailView.as_view(), name='site-detail'),
    # path('site/new/', SitesCreateView.as_view(), name='site-create'), #create site but without adding the image
    path('site/new/', views.site_create, name='site_create'),
    path('site/<int:pk>/update/', SitesUpdateView.as_view(), name='site-update'),
    path('site/<int:pk>/delete/', SitesDeleteView.as_view(), name='site-delete'),
    path('mobilier', MobiliersListView.as_view(), name='touim-mobilier'),
    path('site/<int:site_id>/mobilier_create/', views.mobilier_create, name='mobilier_create'),
    path('mobilier/<int:pk>/delete/', MobiliersDeleteView.as_view(), name='mobilier-delete'),
    path('about/', views.about, name='touim-about'),
    path('layers/', views.layers, name='touim-layers'),
    path('layers2/', views.layers2, name='touim-layers2'),
    path('carto/', views.carto, name='touim-carto'),
    path('biblio/', views.biblio, name='touim-biblio'),
    path('biblio/biblio_create/', views.biblio_create, name='biblio_create')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
