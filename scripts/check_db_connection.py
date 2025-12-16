from datetime import date

from financial_advisor.core.storage_db import (
    insert_transaction,
    fetch_transactions,
)

tx_id = insert_transaction(
    tx_type="income",
    amount=2500,
    category="Salaire",
    tx_date=date.today(),
    description="Test DB",
)

print("Inserted transaction:", tx_id)
print("All transactions:")
print(fetch_transactions())
