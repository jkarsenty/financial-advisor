import json
import pytest
import httpx

from financial_advisor.frontend.api_client import (
    get_summary,
    create_income,
    create_expense,
    APIError,
)


# ---------- Helpers ----------

def mock_transport(handler):
    return httpx.MockTransport(handler)


# ---------- Tests ----------

def test_get_summary_success(monkeypatch):
    def handler(request):
        return httpx.Response(
            200,
            json={
                "total_incomes": 3000.0,
                "total_expenses": 1200.0,
                "remaining": 1800.0,
                "expense_ratio": 0.4,
                "transactions": [],
            },
        )

    transport = mock_transport(handler)
    real_client = httpx.Client

    def client_override(*args, **kwargs):
        return real_client(transport=transport)

    monkeypatch.setattr(httpx, "Client", client_override)

    data = get_summary()

    assert data["total_incomes"] == 3000.0
    assert data["expense_ratio"] == 0.4


def test_get_summary_api_down(monkeypatch):
    def handler(request):
        raise httpx.ConnectError("API down")

    transport = mock_transport(handler)
    real_client = httpx.Client

    def client_override(*args, **kwargs):
        return real_client(transport=transport)

    monkeypatch.setattr(httpx, "Client", client_override)

    with pytest.raises(APIError):
        get_summary()


def test_create_income_success(monkeypatch):
    def handler(request):
        body = json.loads(request.content)
        assert body["amount"] == 2500.0
        assert body["category"] == "Salaire"

        return httpx.Response(201, json=body)

    transport = mock_transport(handler)
    real_client = httpx.Client

    def client_override(*args, **kwargs):
        return real_client(transport=transport)

    monkeypatch.setattr(httpx, "Client", client_override)

    result = create_income(
        {"amount": 2500.0, "category": "Salaire", "description": None}
    )

    assert result["amount"] == 2500.0
    assert result["category"] == "Salaire"


def test_create_expense_http_error(monkeypatch):
    def handler(request):
        return httpx.Response(400, json={"detail": "Invalid category"})

    transport = mock_transport(handler)
    real_client = httpx.Client
    
    def client_override(*args, **kwargs):
        return real_client(transport=transport)

    monkeypatch.setattr(httpx, "Client", client_override)

    with pytest.raises(APIError):
        create_expense(
            {"amount": 500.0, "category": "Invalid", "description": None}
        )
