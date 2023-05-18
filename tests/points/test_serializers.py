"""Points app serializers test cases."""
import pytest

from closest_points.points.serializers import ClosestPointSerializer

pytestmark = pytest.mark.django_db


def test_valid_serializer():
    """Verify a valid serializer."""
    payload = {"points_set": "2,2;-1,30;20,11;4,5"}
    serializer = ClosestPointSerializer(data=payload)
    assert serializer.is_valid()


def test_invalid_serializer():
    """Verify a valid serializer."""
    payload = {"points": "2,2;-1,30;20,11;4,5"}
    serializer = ClosestPointSerializer(data=payload)
    assert not serializer.is_valid()


def test_valid_serializer_create():
    """Verify a valid serializer."""
    payload = {"points_set": "2,2;-1,30;20,11;4,5"}
    serializer = ClosestPointSerializer(data=payload)
    assert serializer.is_valid()

    data = serializer.create(validated_data=payload)
    assert str(data) == "2,2;-1,30;20,11;4,5 (2,2;4,5)"
