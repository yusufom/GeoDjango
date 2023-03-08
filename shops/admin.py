from django.contrib import admin

# Register your models here.
# from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Shop


@admin.register(Shop)
class HotelAdmin(OSMGeoAdmin):
    list_display = ("id", "name", "address", "location")
