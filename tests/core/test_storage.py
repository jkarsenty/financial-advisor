from datetime import date
from pathlib import Path
import os

from financial_advisor.core.incomes import create_income
from financial_advisor.core.storage import save_transactions, load_transactions


def test_storage_roundtrip(tmp_path: Path):
    file = tmp_path / "test.json"

    inc = create_income(1500, "salaire", date.today())
    save_transactions(file, [inc])

    loaded = load_transactions(file)
    assert len(loaded) == 1
    assert loaded[0]["amount"] == 1500
