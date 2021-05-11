from django.contrib import admin

from .models import Sites, Mobiliers, Admini, Staticmap

admin.site.register(Sites)
admin.site.register(Mobiliers)
admin.site.register(Admini)
admin.site.register(Staticmap)
