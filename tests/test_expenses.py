import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_expenses_returns_list(client):
    response = client.get("/expenses")
    assert response.status_code == 200

def test_add_expense(client):
    response = client.post("/expenses", json={
        "amount": 10.00,
        "category": "Food",
        "description": "Test expense",
        "date": "2026-02-25"
    })
    assert response.status_code == 201

def test_add_expense_missing_fields(client):
    response = client.post("/expenses", json={
        "amount": 10.00
    })
    assert response.status_code == 400

def test_delete_nonexistent_expense(client):
    response = client.delete("/expenses/999")
    assert response.status_code == 404