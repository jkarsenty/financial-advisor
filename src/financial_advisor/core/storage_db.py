"""
PostgreSQL storage layer for financial transactions.

Provides basic CRUD operations (Create, Read).
"""

from datetime import date
from typing import List, Optional
from uuid import UUID, uuid4

from financial_advisor.api.db import get_cursor


TransactionRow = dict  # simple alias pour lisibilité


def insert_transaction(
    *,
    tx_type: str,
    amount: float,
    category: str,
    tx_date: date,
    description: Optional[str] = None,
    tx_id: Optional[UUID] = None,
) -> UUID:
    """
    Insert a transaction into the database.

    Args:
        tx_type: 'income' or 'expense'
        amount: transaction amount
        category: transaction category
        tx_date: business date
        description: optional description
        tx_id: optional UUID (generated if None)

    Returns:
        UUID of the inserted transaction.
    """
    transaction_id = tx_id or uuid4()

    query = """
        INSERT INTO transactions (
            id, type, amount, category, description, date
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    with get_cursor() as cursor:
        cursor.execute(
            query,
            (
                str(transaction_id),
                tx_type,
                amount,
                category,
                description,
                tx_date,
            ),
        )

    return transaction_id


def fetch_transactions() -> List[TransactionRow]:
    """
    Fetch all transactions from the database.

    Returns:
        List of transactions as dictionaries.
    """
    query = """
        SELECT
            id,
            type,
            amount,
            category,
            description,
            date,
            created_at
        FROM transactions
        ORDER BY created_at ASC
    """

    with get_cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    return rows
