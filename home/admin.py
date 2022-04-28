from django.contrib import admin
from django.contrib.gis import admin

# Register your models here.
from .models import Accidents, AccidentNumber

class AccidentNumberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "accident_number",
    )


@admin.register(Accidents)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("id", "region", "location")

admin.site.register(AccidentNumber, AccidentNumberAdmin)
