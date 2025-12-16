import httpx
from typing import Dict, Any
from financial_advisor.frontend.config import API_BASE_URL, TIMEOUT_SECONDS

class APIError(Exception):
    """Erreur levée quand l'API backend échoue ou renvoie une erreur."""

def _request(method: str, url: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:    

    try:
        with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
            response = client.request(method, url, json=payload)
            response.raise_for_status()
            return response.json()

    except httpx.ConnectError:
        raise APIError("Impossible de contacter l’API (serveur arrêté ?)")

    except httpx.TimeoutException:
        raise APIError("Temps de réponse dépassé")

    except httpx.HTTPStatusError as exc:
        raise APIError(f"Erreur API ({exc.response.status_code})")
    
    except httpx.HTTPError as exc:
        raise APIError(f"Erreur de communication avec l’API : {str(exc)}")
        

def create_income(payload: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", f"{API_BASE_URL}/api/income", payload)


def create_expense(payload: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", f"{API_BASE_URL}/api/expense", payload)


def get_summary() -> Dict[str, Any]:
    return _request("GET", f"{API_BASE_URL}/api/summary")
