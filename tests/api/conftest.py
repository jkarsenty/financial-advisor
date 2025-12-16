import os
import pytest
from fastapi.testclient import TestClient

from financial_advisor.api.main import app

from financial_advisor.api.db import get_connection


@pytest.fixture(scope="session")
def client() -> TestClient:
    """FastAPI test client."""
    return TestClient(app)


@pytest.fixture(scope="function")
def clean_db():
    """
    Truncate transactions table before each test.
    """
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE transactions RESTART IDENTITY CASCADE;")
        conn.commit()
    yield