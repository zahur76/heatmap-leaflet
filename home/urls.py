from django.urls import path

from . import views
from .views import MarkerViewSet

urlpatterns = [
    path("", views.index, name="home"),
    path("markers", MarkerViewSet.as_view({'get': 'list'}), name="markers"),
    path("markerJson", views.markerJson, name="markersJson"),
]
