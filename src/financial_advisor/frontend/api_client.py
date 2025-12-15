import httpx
from typing import Dict, Any
from financial_advisor.frontend.config import API_BASE_URL, TIMEOUT_SECONDS


def create_income(payload: Dict[str, Any]) -> Dict[str, Any]:
    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        r = client.post(f"{API_BASE_URL}/api/income", json=payload)
        r.raise_for_status()
        return r.json()


def create_expense(payload: Dict[str, Any]) -> Dict[str, Any]:
    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        r = client.post(f"{API_BASE_URL}/api/expense", json=payload)
        r.raise_for_status()
        return r.json()


def get_summary() -> Dict[str, Any]:
    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        r = client.get(f"{API_BASE_URL}/api/summary")
        r.raise_for_status()
        return r.json()
