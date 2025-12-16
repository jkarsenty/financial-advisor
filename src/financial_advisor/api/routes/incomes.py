"""
Income-related API routes.

These routes expose endpoints for creating and retrieving incomes.
The logic layer (financial_advisor.core) performs the actual computations.
Persistence is handled via PostgreSQL.

TODO:
- Add authentication layer if needed (Step 5+)
"""
from datetime import date
from typing import List

from fastapi import APIRouter, HTTPException
from financial_advisor.api.schemas.income_schema import IncomeInput, IncomeResponse

from financial_advisor.core.storage_db import (
    insert_transaction, 
    fetch_transactions,
)

router = APIRouter(prefix="/income", tags=["income"])

@router.post("", response_model=IncomeResponse)
def add_income(payload: IncomeInput) -> IncomeResponse:
    """
    Create a new income entry and persist it in PostgreSQL.

    Args:
        payload (IncomeInput): Incoming income data validated by Pydantic.

    Returns:
        IncomeResponse: The created income entry.

    Raises:
        HTTPException: If storage fails.

    """
    try:
        tx_id = insert_transaction(
            tx_type="income",
            amount=payload.amount,
            category=payload.category,
            tx_date=payload.date_ or date.today(),
            description=payload.description,
        )

        return IncomeResponse(
            id=tx_id,
            amount=payload.amount,
            category=payload.category,
            description=payload.description,
            date_=payload.date_ or date.today(),
            type="income",
        )

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("", response_model=List[IncomeResponse])
def list_incomes() -> List[IncomeResponse]:
    """
    Return all stored incomes from PostgreSQL.

    Returns:
        list[IncomeResponse]: List of income entries.
    """
    try:
        transactions = fetch_transactions()

        incomes = [
            IncomeResponse(
                id=t["id"],
                amount=t["amount"],
                category=t["category"],
                description=t.get("description"),
                date_=t["date"],
                type=t["type"],
            )
            for t in transactions
            if t["type"] == "income"
        ]

        return incomes

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))