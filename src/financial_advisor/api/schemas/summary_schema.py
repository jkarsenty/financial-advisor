"""
Pydantic schemas for the financial summary endpoint.

These schemas define the response structure for aggregated financial data:
totals, ratios, and the list of all recorded transactions.

TODO:
- Add transaction IDs once a database is introduced (Step 3)
- Add date fields when temporal tracking is implemented
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class TransactionItem(BaseModel):
    """
    Represents a generic income or expense entry included in the summary.
    
    Note:
        An optional date or ID field can be added later.
    """

    amount: float = Field(..., description="Transaction amount.")
    category: str = Field(..., description="Transaction category.")
    description: Optional[str] = Field(None, description="Optional transaction description.")
    type: str = Field(..., description="'income' or 'expense'")


class SummaryResponse(BaseModel):
    """
    Represents the aggregated financial summary returned by the API.
    """

    total_income: float = Field(..., description="Sum of all recorded incomes.")
    total_expenses: float = Field(..., description="Sum of all recorded expenses.")
    remaining: float = Field(..., description="Remaining balance (income - expenses).")
    fixed_ratio: Optional[float] = Field(
        None, description="Ratio of fixed expenses to total expenses (if applicable)."
    )
    transactions: List[TransactionItem] = Field(
        ..., description="List of all recorded incomes and expenses."
    )
