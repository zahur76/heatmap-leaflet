from django.contrib import admin
from django.contrib.gis import admin

# Register your models here.
from .models import Accidents


@admin.register(Accidents)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("id", "region", "accident_number", "location")
