"""Points app config."""
from django.apps import AppConfig


class PointsConfig(AppConfig):
    """Points app config class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "closest_points.points"
