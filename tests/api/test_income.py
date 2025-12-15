def test_create_income(client):
    payload = {
        "amount": 2500,
        "category": "salaire",
        "description": "Salaire test",
    }

    response = client.post("/api/income", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["amount"] == 2500
    assert data["category"] == "salaire"
    assert "date_" in data