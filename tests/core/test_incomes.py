from datetime import date
import pytest

from financial_advisor.core.incomes import create_income


def test_create_valid_income():
    inc = create_income(2000, "salaire", date.today())
    assert inc["amount"] == 2000
    assert inc["category"] == "salaire"


def test_income_must_be_positive():
    with pytest.raises(ValueError):
        create_income(-50, "salaire", date.today())


def test_income_category_invalid():
    with pytest.raises(ValueError):
        create_income(1000, "foo", date.today())
