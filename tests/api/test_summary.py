def test_get_summary(client, clean_db):
    client.post(
        "/api/income",
        json={"amount": 2000, "category": "salaire"},
    )
    client.post(
        "/api/expense",
        json={"amount": 500, "category": "logement"},
    )

    response = client.get("/api/summary")

    assert response.status_code == 200
    
    data = response.json()
    assert "total_incomes" in data
    assert "total_expenses" in data
    assert "remaining" in data
    assert "expense_ratio" in data
    assert 0.0 <= data["expense_ratio"] <= 1.0

    transactions = data["transactions"]
    assert isinstance(transactions, list)
    assert len(transactions) >= 2

    for t in transactions:
        assert "type" in t
        assert t["type"] in ("income", "expense")
