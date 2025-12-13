"""
Module: calculations
Description:
    Contient toutes les fonctions de calcul financier utilisées par l'application.

    Approche fonctionnelle : chaque fonction reçoit des listes de transactions
    (dictionnaires Transaction) et retourne une valeur calculée.

    Fonctions principales :
    - total_incomes
    - total_expenses
    - living_balance (reste à vivre)
    - expense_ratio (ratio dépenses / revenus)
"""

from typing import List

from .models import Transaction


# -------------------------------------------------------------------
# Totaux simples
# -------------------------------------------------------------------

def total_incomes(incomes: List[Transaction]) -> float:
    """
    Calcule le total des revenus.

    Args:
        incomes: Liste de transactions représentant des revenus.

    Returns:
        Somme des montants.
    """
    return sum(t["amount"] for t in incomes)


def total_expenses(expenses: List[Transaction]) -> float:
    """
    Calcule le total des dépenses.

    Note:
        Les dépenses sont supposées négatives (normalisées dans expenses.py).

    Args:
        expenses: Liste de transactions négatives.

    Returns:
        Somme des montants de dépenses.
    """
    return sum(t["amount"] for t in expenses)


# -------------------------------------------------------------------
# Calculs combinés
# -------------------------------------------------------------------

def living_balance(incomes: List[Transaction], expenses: List[Transaction]) -> float:
    """
    Calcule le reste à vivre.

    Formule :
        total_incomes - abs(total_expenses)

    Returns:
        Reste à vivre.
    """
    return total_incomes(incomes) + total_expenses(expenses)


# -------------------------------------------------------------------
# Ratios & statistiques
# -------------------------------------------------------------------

def expense_ratio(incomes: List[Transaction], expenses: List[Transaction]) -> float:
    """
    Calcule le ratio dépenses / revenus.

    Returns:
        Un pourcentage exprimé entre 0 et 1.
        Si aucun revenu, retourne 0 pour éviter une division par zéro.
    """
    total_inc = total_incomes(incomes)
    if total_inc == 0:
        return 0.0

    total_exp = abs(total_expenses(expenses))
    return total_exp / total_inc


def summary(incomes: List[Transaction], expenses: List[Transaction]) -> dict:
    """
    Génère un résumé financier utilisable par l'API ou le frontend.

    Returns:
        dict contenant :
            - total_incomes
            - total_expenses
            - living_balance
            - expense_ratio
    """
    total_inc = total_incomes(incomes)
    total_exp = total_expenses(expenses)
    balance = living_balance(incomes, expenses)
    ratio = expense_ratio(incomes, expenses)

    return {
        "total_incomes": total_inc,
        "total_expenses": total_exp,
        "living_balance": balance,
        "expense_ratio": ratio,
    }
