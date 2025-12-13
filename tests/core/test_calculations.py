from datetime import date

from financial_advisor.core.incomes import create_income
from financial_advisor.core.expenses import create_expense
from financial_advisor.core.calculations import (
    total_incomes,
    total_expenses,
    living_balance,
    expense_ratio,
)


def test_totals():
    inc1 = create_income(2000, "salaire", date.today())
    inc2 = create_income(500, "prime", date.today())
    assert total_incomes([inc1, inc2]) == 2500

    exp1 = create_expense(100, "courses", date.today())  # devient négatif
    exp2 = create_expense(50, "transport", date.today())
    assert total_expenses([exp1, exp2]) == -150


def test_living_balance():
    inc = create_income(2000, "salaire", date.today())
    exp = create_expense(100, "courses", date.today())
    assert living_balance([inc], [exp]) == 2000 - 100


def test_expense_ratio():
    inc = create_income(2000, "salaire", date.today())
    exp = create_expense(100, "courses", date.today())
    assert expense_ratio([inc], [exp]) == 100 / 2000
