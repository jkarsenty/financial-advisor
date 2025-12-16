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

from financial_advisor.core.storage_db import fetch_transactions
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
        raw_transactions = fetch_transactions()

        # Convert amounts to float for calculations
        transactions = [
            {
                **t,
                "amount": float(t["amount"]),
            }
            for t in raw_transactions
        ]


        # Compute summary using core logic
        summary_data = compute_summary(transactions)

        # Convert raw transactions → Pydantic TransactionItem instances
        items = [
            TransactionItem(
                id=t["id"],
                amount=t["amount"],
                category=t["category"],
                description=t.get("description"),
                date=t["date"],
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
