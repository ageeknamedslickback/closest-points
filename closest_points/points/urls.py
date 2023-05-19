"""Points app URL config."""
from django.urls import path

from closest_points.points.views import ClosestPointsView

urlpatterns = [
    path("closest-points/", ClosestPointsView.as_view(), name="closest-point"),
]
