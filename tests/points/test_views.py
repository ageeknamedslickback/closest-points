"""Points app views test cases."""
import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    """Test client."""
    return APIClient()


def test_closest_point_post_api(client):
    """Verify closest points API."""
    url = reverse("closest-point")
    data = {"points_set": "2,2;-1,30;20,11;4,5"}
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "points_set": "2,2;-1,30;20,11;4,5",
        "closest_points": "2,2;4,5",
    }


def test_closest_point_get_api(client):
    """Verify closest points API."""
    url = reverse("closest-point")
    data = {"points_set": "2,2;-1,30;20,11;4,5"}
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "points_set": "2,2;-1,30;20,11;4,5",
        "closest_points": "2,2;4,5",
    }

    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
