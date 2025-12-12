"""
Module: categories
Description: Définit les catégories financières et leur validation.
"""

from typing import List


# Catégories de revenus
INCOME_CATEGORIES: List[str] = [
    "salaire",
    "prime",
    "revenu_locatif",
    "autre_revenu",
]

# Catégories de dépenses
EXPENSE_CATEGORIES: List[str] = [
    "logement",
    "services_publics",
    "courses",
    "transport",
    "divertissement",
    "sante",
    "abonnements",
    "autre_depense",
]


def normalize_category(category: str) -> str:
    """
    Nettoie une catégorie :
    - trim
    - lowercase
    """
    return category.strip().lower()


def is_valid_income_category(category: str) -> bool:
    """Vérifie si une catégorie appartient aux revenus."""
    return normalize_category(category) in INCOME_CATEGORIES


def is_valid_expense_category(category: str) -> bool:
    """Vérifie si une catégorie appartient aux dépenses."""
    return normalize_category(category) in EXPENSE_CATEGORIES
