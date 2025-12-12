"""
main.py
Script temporaire pour tester manuellement la logique métier (Step 0).

Attention :
Ce fichier sera supprimé ou remplacé lors des étapes API (FastAPI) ou Front (Streamlit).
"""

from datetime import date
from pathlib import Path
import random

from financial_advisor.core.incomes import create_income
from financial_advisor.core.expenses import create_expense
from financial_advisor.core.calculations import summary
from financial_advisor.core.storage import save_transactions, load_transactions

# ---------------------------------------------------------------------
# Génération aléatoire pour faciliter les tests
# ---------------------------------------------------------------------

INCOME_CATEGORIES = ["salaire", "prime", "revenu_locatif", "autre_revenu"]
EXPENSE_CATEGORIES = ["logement", "services_publics", "courses", "transport", "divertissement", "sante", "abonnements", "autre_depense"]

def random_income() -> dict:
    """Génère un revenu aléatoire dans une fourchette simple."""
    amount = random.randint(1500, 4000)  # revenu réaliste
    category = random.choice(INCOME_CATEGORIES)
    description = f"Revenu auto-genere ({category})"
    return create_income(amount, category, date.today(), description)


def random_expense() -> dict:
    """Génère une dépense aléatoire simple."""
    amount = random.randint(10, 200)
    category = random.choice(EXPENSE_CATEGORIES)
    description = f"Depense auto-generee ({category})"
    return create_expense(amount, category, date.today(), description)


# ---------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------

def run_demo() -> None:
    """Démontre les fonctionnalités de base."""

    print("\n=== Génération aléatoire de transactions ===")

    incomes = [random_income() for _ in range(2)]
    expenses = [random_expense() for _ in range(3)]

    print("Revenus générés :")
    for inc in incomes:
        print("  ->", inc)

    print("\nDépenses générées :")
    for exp in expenses:
        print("  ->", exp)

    print("\n=== Calculs ===")
    result = summary(incomes, expenses)
    print(result)

    print("\n=== Stockage JSON ===")
    file = Path("data/demo.json")
    save_transactions(file, incomes + expenses)
    print("Données rechargées :", load_transactions(file))


if __name__ == "__main__":
    run_demo()
