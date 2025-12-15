"""
Module: models
Description: Définit les structures de données fonctionnelles utilisées pour les
transactions financières (revenus, dépenses). Aucune logique métier ici, uniquement
la forme commune des données.

Ce module utilise des dictionnaires typés plutôt que des classes pour garder un style
fonctionnel simple et testable.
"""

from typing import TypedDict, Optional, Literal
from datetime import date

class Transaction(TypedDict):
    """Structure générique d'une transaction financière."""
    amount: float
    category: str
    description: Optional[str]
    date_: Optional[str]
    type: Literal["income", "expense"]

# TODO: Étape suivante -> spécialiser Income et Expense via fonctions dans incomes.py et expenses.py
