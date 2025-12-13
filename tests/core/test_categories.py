from financial_advisor.core.categories import (
    is_valid_income_category,
    is_valid_expense_category,
)


def test_valid_income_categories():
    assert is_valid_income_category("salaire")
    assert is_valid_income_category("prime")


def test_invalid_income_categories():
    assert not is_valid_income_category("foo")
    assert not is_valid_income_category("transport")  # catégorie dépense


def test_valid_expense_categories():
    assert is_valid_expense_category("courses")
    assert is_valid_expense_category("transport")


def test_invalid_expense_categories():
    assert not is_valid_expense_category("salaire")
    assert not is_valid_expense_category("foo")
