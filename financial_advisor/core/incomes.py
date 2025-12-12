"""
Module: incomes
Description: Fonctions responsables de la gestion des revenus :
- création d'un revenu
- validation
- normalisation
"""

from datetime import date
from typing import Optional

from .models import Transaction
from .categories import is_valid_income_category, normalize_category


def validate_income_fields(amount: float, category: str) -> None:
    """
    Valide les champs d'un revenu.
    Règles métier :
    - Le montant doit être strictement positif.
    - La catégorie doit être valide.
    """
    if amount <= 0:
        raise ValueError("Le montant d'un revenu doit être strictement positif.")

    if not is_valid_income_category(category):
        raise ValueError(f"Catégorie de revenu invalide : {category}")


def create_income(
    amount: float,
    category: str,
    date_: date,
    description: Optional[str] = None,
) -> Transaction:
    """
    Crée un revenu validé et normalisé sous forme de dictionnaire.

    Raises:
        ValueError: si les champs ne sont pas valides.
    """
    validate_income_fields(amount, category)

    return {
        "amount": amount,
        "category": normalize_category(category),
        "date": date_,
        "description": description,
    }


# a ajouter dans les tests
def validate_income(income: Transaction) -> bool:
    """
    Vérifie la validité d'un revenu.

    TODO:
    - Vérifier montant > 0
    - Vérifier catégorie valide
    - Vérifier format des champs
    """
    return True
