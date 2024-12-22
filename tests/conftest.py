import pytest
from fastapi.testclient import TestClient

from workouts_backend.app import app


@pytest.fixture
def client():
    return TestClient(app)
