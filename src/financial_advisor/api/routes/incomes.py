"""
Income-related API routes.

These routes expose endpoints for creating and retrieving incomes.
The logic layer (financial_advisor.core) performs the actual computations.

TODO:
- Replace JSON storage with a real database (Step 3)
- Add authentication layer if needed (Step 5+)
"""

from fastapi import APIRouter, HTTPException
from financial_advisor.api.schemas.income_schema import IncomeInput, IncomeResponse

from financial_advisor.core.incomes import create_income
from financial_advisor.core.storage import load_transactions, save_transactions

from pathlib import Path


router = APIRouter(prefix="/income", tags=["income"])

# Temporary JSON file used as storage until Postgres is introduced.
DATA_FILE = Path("data/transactions.json")


@router.post("", response_model=IncomeResponse)
def add_income(payload: IncomeInput) -> IncomeResponse:
    """
    Create a new income entry and persist it.

    Args:
        payload (IncomeInput): Incoming income data validated by Pydantic.

    Returns:
        IncomeResponse: The created income entry.

    Raises:
        HTTPException: If storage fails.
    """
    try:
        # create income using core logic
        income = create_income(
            amount=payload.amount,
            category=payload.category,
            description=payload.description,
            date_=payload.date_
        )

        # load existing transactions
        transactions = load_transactions(DATA_FILE)

        # append new income
        transactions.append(income)

        # save back to file
        save_transactions(DATA_FILE, transactions)

        # The API returns only the fields defined in the response schema
        return IncomeResponse(**income) 

    except Exception as exc:  # broad catch is OK temporarily before DB
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("", response_model=list[IncomeResponse])
def list_incomes() -> list[IncomeResponse]:
    """
    Return all stored incomes.

    Returns:
        list[IncomeResponse]: List of income entries.
    """
    transactions = load_transactions(DATA_FILE)

    incomes = [
        IncomeResponse(**t) for t in transactions if t.get("type") == "income"
    ]

    return incomes
