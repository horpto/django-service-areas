from django.contrib import admin

from django.contrib.gis import admin as gis_admin
from .models import ServiceArea

gis_admin.site.register(ServiceArea, gis_admin.GeoModelAdmin)