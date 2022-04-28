"""Markers serializers."""

from rest_framework_gis import serializers

from .models import Accidents


class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""

        fields = (
            "id",
            "region",
        )
        geo_field = "location"
        model = Accidents
        