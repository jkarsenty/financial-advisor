def test_create_expense(client):
    payload = {
        "amount": 800,
        "category": "logement",
        "description": "Loyer test",
    }

    response = client.post("/api/expense", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["amount"] == 800
    assert data["category"] == "logement"
    assert "date_" in data
