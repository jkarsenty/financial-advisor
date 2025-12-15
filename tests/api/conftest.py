import json
import pytest
from pathlib import Path
from fastapi.testclient import TestClient

from financial_advisor.api.main import app


DATA_FILE = Path("data/transactions.json")

@pytest.fixture(scope="session")
def client() -> TestClient:
    """FastAPI test client."""
    return TestClient(app)


@pytest.fixture(scope="function")
def clean_storage():
    """
    Reset the transactions JSON file before each test.

    Ensures test isolation and deterministic behavior.
    """
    # Ensure data directory exists
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Reset file content
    DATA_FILE.write_text("[]", encoding="utf-8")

    yield

    # Optional cleanup after test (not strictly necessary here)
    DATA_FILE.write_text("[]", encoding="utf-8")
