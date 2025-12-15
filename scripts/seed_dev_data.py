from pathlib import Path
from datetime import date
import json

DATA_FILE = Path("data/transactions.json")

transactions = [
    {
        "amount": 2500,
        "category": "salaire",
        "description": "Salaire mensuel",
        "date_": str(date.today()),
        "type": "income",
    },
    {
        "amount": 400,
        "category": "freelance",
        "description": "Mission ponctuelle",
        "date_": str(date.today()),
        "type": "income",
    },
    {
        "amount": -900,
        "category": "logement",
        "description": "Loyer",
        "date_": str(date.today()),
        "type": "expense",
    },
    {
        "amount": -150,
        "category": "transport",
        "description": "Essence",
        "date_": str(date.today()),
        "type": "expense",
    },
]

DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
DATA_FILE.write_text(json.dumps(transactions, indent=2), encoding="utf-8")

print("Dev data seeded")
