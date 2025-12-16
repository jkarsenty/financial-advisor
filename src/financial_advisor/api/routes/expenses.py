"""
Expense-related API routes.

These routes expose endpoints for creating and retrieving expenses.
All business logic remains in financial_advisor.core.
Persistence is handled via PostgreSQL.

TODO:
- Add authentication or per-user storage (future step)
"""
from datetime import date
from typing import List

from fastapi import APIRouter, HTTPException
from financial_advisor.api.schemas.expense_schema import ExpenseInput, ExpenseResponse

from financial_advisor.core.storage_db import (
    insert_transaction,
    fetch_transactions,
)


router = APIRouter(prefix="/expense", tags=["expense"])


@router.post("", response_model=ExpenseResponse)
def add_expense(payload: ExpenseInput) -> ExpenseResponse:
    """
    Create a new expense entry and persist it in PostgreSQL.
    
    Args:
        payload (ExpenseInput): Incoming expense data validated by Pydantic.

    Returns:
        ExpenseResponse: The created expense entry.

    Raises:
        HTTPException: On storage failure.
    """
    try:
        tx_id = insert_transaction(
            tx_type="expense",
            amount=payload.amount,
            category=payload.category,
            tx_date=payload.date_ or date.today(),
            description=payload.description,
        )

        return ExpenseResponse(
            id=tx_id,
            amount=payload.amount,
            category=payload.category,
            description=payload.description,
            date_=payload.date_ or date.today(),
            type="expense",
        )

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("", response_model=list[ExpenseResponse])
def list_expenses() -> list[ExpenseResponse]:
    """
    Return all stored expenses from PostgreSQL.

    Returns:
        list[ExpenseResponse]: List of expense entries only.
    """
    try:
        transactions = fetch_transactions()

        expenses = [
            ExpenseResponse(
                id=t["id"],
                amount=t["amount"],
                category=t["category"],
                description=t.get("description"),
                date_=t["date"],
                type=t["type"],
            )
            for t in transactions
            if t["type"] == "expense"
        ]

        return expenses

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
