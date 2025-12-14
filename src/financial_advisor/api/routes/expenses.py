"""
Expense-related API routes.

These routes expose endpoints for creating and retrieving expenses.
All business logic remains in financial_advisor.core.

TODO:
- Replace JSON storage with a real database (Step 3)
- Add authentication or per-user storage (future step)
"""

from fastapi import APIRouter, HTTPException
from financial_advisor.api.schemas.expense_schema import ExpenseInput, ExpenseResponse

from financial_advisor.core.expenses import create_expense
from financial_advisor.core.storage import load_transactions, save_transactions

from pathlib import Path


router = APIRouter(prefix="/expense", tags=["expense"])

# Temporary JSON file, replaced later by a database.
DATA_FILE = Path("data/transactions.json")


@router.post("", response_model=ExpenseResponse)
def add_expense(payload: ExpenseInput) -> ExpenseResponse:
    """
    Create a new expense entry and persist it.

    Args:
        payload (ExpenseInput): Incoming expense data validated by Pydantic.

    Returns:
        ExpenseResponse: The created expense entry.

    Raises:
        HTTPException: On storage failure.
    """
    try:
        expense = create_expense(
            amount=payload.amount,
            category=payload.category,
            description=payload.description,
            date_=payload.date_
        )

        transactions = load_transactions(DATA_FILE)
        transactions.append(expense)
        save_transactions(DATA_FILE, transactions)

        return ExpenseResponse(**expense)

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("", response_model=list[ExpenseResponse])
def list_expenses() -> list[ExpenseResponse]:
    """
    Return all stored expenses.

    Returns:
        list[ExpenseResponse]: List of expense entries only.
    """
    transactions = load_transactions(DATA_FILE)

    expenses = [
        ExpenseResponse(**t) for t in transactions if t.get("type") == "expense"
    ]

    return expenses
