from django.contrib import admin

from .models import Map, Building

# Register your models here.
admin.site.register(Building)
admin.site.register(Map)