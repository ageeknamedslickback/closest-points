"""Points admin interface."""
from django.contrib import admin

from closest_points.points.models import ClosestPoint


class ClosestPointAdmin(admin.ModelAdmin):
    """Closest point model admin config."""

    pass


admin.site.register(ClosestPoint, ClosestPointAdmin)
