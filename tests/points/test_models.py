"""Points model tests."""
import pytest
from model_bakery import baker

from closest_points.points.models import ClosestPoint

pytestmark = pytest.mark.django_db


@pytest.fixture
def point():
    """Test points."""
    return baker.make(
        ClosestPoint,
        points_set="2,2;-1,30;20,11;4,5",
    )


def test_save_closest_points(point):
    """Verify saving of points."""
    assert ClosestPoint.objects.count() == 1
    assert point.points_set == "2,2;-1,30;20,11;4,5"
    assert point.closest_points == "2,2;4,5"


def test_closest_points_str(point):
    """Verify model str representation."""
    assert str(point) == "2,2;-1,30;20,11;4,5 (2,2;4,5)"


def test_cartesian_points(point):
    """Verify parsed cartesian points."""
    assert point.cartesian_points == [(2, 2), (-1, 30), (20, 11), (4, 5)]


def test_calculate_distance(point):
    """Verify points distance calculation."""
    distance = point.calculate_distance(2, 2, -1, 30)
    assert distance == 31.0


def test_get_points_distance(point):
    """Verfiy getting distances between points."""
    distance_and_points = point.get_points_distances()
    assert isinstance(distance_and_points, list)
    assert len(distance_and_points) == 12
    assert distance_and_points[0] == [28.160255680657446, (2, 2), (-1, 30)]


def test_calculate_closest_pair_of_points(point):
    """Verify closest points."""
    closest_points = point.calculate_closest_pair_of_points()
    assert closest_points == [((2, 2), (4, 5))]


def test_closest_pair_str(point):
    """Verify closest pair str representation."""
    point_str = point.closest_pair_str
    assert point_str == "2,2;4,5"
