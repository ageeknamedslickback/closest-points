"""Points app views."""
from rest_framework import generics

from closest_points.points.models import ClosestPoint
from closest_points.points.serializers import ClosestPointSerializer


class ClosestPointsView(generics.ListCreateAPIView):
    """Closest points generic list and create API view."""

    queryset = ClosestPoint.objects.all()
    serializer_class = ClosestPointSerializer
