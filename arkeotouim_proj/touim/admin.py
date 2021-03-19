from django.contrib import admin

from .models import Sites, Mobiliers, Admini, Biblio, Staticmap

admin.site.register(Sites)
admin.site.register(Mobiliers)
admin.site.register(Admini)
admin.site.register(Biblio)
admin.site.register(Staticmap)
