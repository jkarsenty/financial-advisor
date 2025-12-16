"""
Database connection utilities for the API.

Centralizes PostgreSQL connection handling.
"""

import os
from typing import Generator
from contextlib import contextmanager

import psycopg
from psycopg.rows import dict_row


def get_database_url() -> str:
    """
    Return the DATABASE_URL from environment variables.

    Raises:
        RuntimeError: if DATABASE_URL is not defined.
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL environment variable is not set")
    return db_url


def get_connection() -> psycopg.Connection:
    """
    Create and return a new PostgreSQL connection.

    Returns:
        psycopg.Connection: active DB connection.
    """
    return psycopg.connect(
        get_database_url(),
        row_factory=dict_row,
    )


@contextmanager
def get_cursor() -> Generator[psycopg.Cursor, None, None]:
    """
    Context manager yielding a database cursor.

    Commits automatically on success.
    Rolls back on error.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            yield cursor
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
