import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from workouts_backend.app import app
from workouts_backend.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
