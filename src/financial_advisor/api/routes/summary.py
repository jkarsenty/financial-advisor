"""
Summary-related API routes.

This route exposes the aggregated financial summary:
total incomes, total expenses, remaining balance,
and an itemized list of all transactions.

TODO:
- Add date-based filters (e.g., /summary?month=...)
- Move storage to PostgreSQL (Step 3)
- Add ML-powered recommendations (Step 4)
"""

from fastapi import APIRouter, HTTPException
from pathlib import Path

from financial_advisor.core.storage import load_transactions
from financial_advisor.core.calculations import summary as compute_summary

from financial_advisor.api.schemas.summary_schema import (
    SummaryResponse,
    TransactionItem,
)


router = APIRouter(prefix="/summary", tags=["summary"])

# Temporary JSON storage
DATA_FILE = Path("data/transactions.json")


@router.get("", response_model=SummaryResponse)
def get_summary() -> SummaryResponse:
    """
    Return the aggregated financial summary.

    Returns:
        SummaryResponse: Totals, ratios, and all transactions.

    Raises:
        HTTPException: On failure to compute the summary.
    """
    try:
        transactions = load_transactions(DATA_FILE)

        # Compute summary using core logic
        summary_data = compute_summary(transactions)

        # Convert raw transactions → Pydantic TransactionItem instances
        items = [
            TransactionItem(
                amount=t["amount"],
                category=t["category"],
                description=t.get("description"),
                type=t["type"],
            )
            for t in transactions
        ]

        return SummaryResponse(
            total_incomes=summary_data["total_incomes"],
            total_expenses=summary_data["total_expenses"],
            remaining=summary_data["remaining"],
            expense_ratio=summary_data["expense_ratio"],
            transactions=items,
        )

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
