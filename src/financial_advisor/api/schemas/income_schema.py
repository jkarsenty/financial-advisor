"""
Pydantic schemas for income-related API operations.

These schemas validate incoming data for income creation requests
and define the structure of API responses.
"""

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from uuid import UUID


class IncomeInput(BaseModel):
    """Schema representing an income entry provided by the user."""

    amount: float = Field(..., gt=0, description="Income amount (must be positive).")
    category: str = Field(..., description="Income category (e.g., salaire, bonus).")
    description: Optional[str] = Field(None, description="Optional income description.")
    date_: date = Field(default_factory=date.today)


class IncomeResponse(BaseModel):
    """
    Schema representing an income entry returned by the API.
    """
    
    id: UUID
    amount: float
    category: str
    description: Optional[str]
    date_: date 
    type: str = "income"

