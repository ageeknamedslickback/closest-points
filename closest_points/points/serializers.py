"""Points app serializers."""
from rest_framework.serializers import ModelSerializer

from closest_points.points.models import ClosestPoint


class ClosestPointSerializer(ModelSerializer):
    """Closest points serializer."""

    class Meta:
        """Serializer meta options."""

        model = ClosestPoint
        fields = ["points_set", "closest_points"]
        read_only_fields = ["closest_points"]
