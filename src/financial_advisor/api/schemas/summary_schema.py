"""
Pydantic schemas for the financial summary endpoint.

These schemas define the response structure for aggregated financial data:
totals, ratios, and the list of all recorded transactions.
"""

from datetime import date as Date
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """
    Represents a generic income or expense entry included in the summary.
    """
    id: UUID = Field(..., description="Unique transaction identifier.")
    amount: float = Field(..., description="Transaction amount.")
    category: str = Field(..., description="Transaction category.")
    description: Optional[str] = Field(None, description="Optional transaction description.")
    date: Date = Field(..., description="Transaction date.")
    type: str = Field(..., description="'income' or 'expense'")


class SummaryResponse(BaseModel):
    """
    Represents the aggregated financial summary returned by the API.
    """

    total_incomes: float = Field(..., description="Sum of all recorded incomes.")
    total_expenses: float = Field(..., description="Sum of all recorded expenses.")
    remaining: float = Field(..., description="Remaining balance (income - expenses).")
    expense_ratio: Optional[float] = Field(
        None, description="Ratio of expenses to total incomes (if applicable)."
    )
    transactions: List[TransactionItem] = Field(
        ..., description="List of all recorded incomes and expenses."
    )
