"""Closest point project models."""
import heapq
import math

from django.db import models


class ClosestPoint(models.Model):
    """A set of semicolon separated points."""

    points_set = models.CharField(max_length=255)
    closest_points = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        """Human readable representation of the model."""
        return f"{self.points_set} ({self.closest_points})"

    @property
    def cartesian_points(self) -> list:
        """Parse point sets to [(x1,y1), (x2,y2)] format."""
        points = []
        split_points = self.points_set.split(";")
        for each in split_points:
            points.append(eval(each))

        return points

    def calculate_distance(
        self, x1: float, y1: float, x2: float, y2: float
    ) -> float:
        """Calculate the distance between two points."""
        return math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)

    def get_points_distances(self) -> float:
        """Get a list of distances between points."""
        distances = []
        for x in self.cartesian_points:
            for y in self.cartesian_points:
                distance = self.calculate_distance(x[0], y[0], x[1], y[1])
                # if 0.0 its the distance of the point to itself
                if distance == 0.0:
                    continue
                distances.append([distance, (x[0], x[1]), (y[0], y[1])])
        return distances

    def calculate_closest_pair_of_points(self) -> list:
        """Calculate closest pair of points."""
        distance_and_points = self.get_points_distances()
        heapq.heapify(distance_and_points)
        _, x, y = heapq.heappop(distance_and_points)
        results = []
        results.append((x, y))

        return results

    @property
    def closest_pair_str(self) -> str:
        """Str formatted closest points 'x, y'."""
        closest_points = self.calculate_closest_pair_of_points()[0]
        first_points = []
        for point in closest_points[0]:
            first_points.append(str(point))

        second_points = []
        for point in closest_points[1]:
            second_points.append(str(point))

        return f"{','.join(first_points)};{','.join(second_points)}"

    def save(self) -> None:
        """Override default save method."""
        self.closest_points = self.closest_pair_str
        return super().save()
