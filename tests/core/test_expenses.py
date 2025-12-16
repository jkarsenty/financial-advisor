from datetime import date
import pytest

from financial_advisor.core.expenses import create_expense


def test_create_valid_expense():
    exp = create_expense(50, "courses", date.today())
    assert exp["amount"] > 0
    assert exp["category"] == "courses"


def test_expense_category_invalid():
    with pytest.raises(ValueError):
        create_expense(30, "foo", date.today())
