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


def validate_expense_fields(amount: float, category: str) -> None:
    """
    Règles métier :
    - Le montant doit être strictement positif.
    - La catégorie doit être valide.
    """
    if amount <= 0:
        raise ValueError("Le montant d'une dépense doit être positif")
    
    if not is_valid_expense_category(category):
        raise ValueError(f"Catégorie de dépense invalide : {category}")


def create_expense(
    amount: float,
    category: str,
    date_: date,
    description: Optional[str] = None,
) -> Transaction:
    """
    Crée une dépense validée.

    Raises:
        ValueError: si la catégorie est invalide.
    """
    validate_expense_fields(amount, category)

    return {
        "amount": amount,
        "category": normalize_category(category),
        "description": description,
        "date_": str(date_),
        "type": "expense"
    }
