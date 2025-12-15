"""
Module: expenses
Description: Fonctions chargées de la gestion des dépenses :
- créer les dépenses
- valider les dépenses
"""

from datetime import date
from typing import Optional

from .models import Transaction
from .categories import is_valid_expense_category, normalize_category


def normalize_amount(amount: float) -> float:
    """Transforme un montant en montant négatif si nécessaire."""
    return -abs(amount)


def validate_expense_fields(amount: float, category: str) -> None:
    """
    Règles métier :
    - Le montant doit être négatif (ou sera normalisé).
    - La catégorie doit être valide.
    """
    if not is_valid_expense_category(category):
        raise ValueError(f"Catégorie de dépense invalide : {category}")

    # Le montant sera normalisé, donc pas d'erreur si > 0.


def create_expense(
    amount: float,
    category: str,
    date_: date,
    description: Optional[str] = None,
) -> Transaction:
    """
    Crée une dépense validée et normalisée.

    Raises:
        ValueError: si la catégorie est invalide.
    """
    validate_expense_fields(amount, category)

    normalized_amount = normalize_amount(amount)

    return {
        "amount": normalized_amount,
        "category": normalize_category(category),
        "description": description,
        "date_": str(date_),
        "type": "expense"
    }
