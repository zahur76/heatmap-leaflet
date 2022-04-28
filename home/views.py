from django.shortcuts import render, get_object_or_404
"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import AccidentNumber, Accidents
from .serializers import MarkerSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here
def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Accidents.objects.all()
    serializer_class = MarkerSerializer


def markerJson(request):
    """ Return json format of accidents """

    data = []

    all_markers = AccidentNumber.objects.all()

    for marker in all_markers:
        entry = get_object_or_404(Accidents, id=marker.accidents.id)
        data.append({'lat': entry.location.coords[1], 'lng': entry.location.coords[0], 'number': marker.accident_number})

    return JsonResponse(data, safe=False)