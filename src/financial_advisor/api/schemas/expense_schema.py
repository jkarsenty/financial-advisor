"""
Pydantic schemas for expense-related API operations.

These schemas validate incoming data for expense creation requests
and define the structure of API responses.
"""

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from uuid import UUID


class ExpenseInput(BaseModel):
    """Schema representing an expense entry provided by the user."""

    amount: float = Field(..., gt=0, description="Expense amount (must be positive).")
    category: str = Field(..., description="Expense category (e.g., logement, transport).")
    description: Optional[str] = Field(None, description="Optional expense description.")
    date_: date = Field(default_factory=date.today, description="Date of the expense.")



class ExpenseResponse(BaseModel):
    """
    Schema representing an expense entry returned by the API.
    """
    id: UUID
    amount: float
    category: str
    description: Optional[str]
    date_: date
    type: str = "expense"
