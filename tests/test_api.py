from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Currency Converter API!"}


def test_convert(monkeypatch):
    from app.services import converter

    monkeypatch.setattr(converter, "fetch_conversion_rate", lambda f, t: 2.0)
    response = client.post(
        "/convert", params={"amount": 5, "from_currency": "AUD", "to_currency": "NPR"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["from_currency"] == "AUD"
    assert data["to_currency"] == "NPR"
    assert data["amount"] == 5
    assert data["converted_amount"] == 10.0
    assert data["rate"] == 2.0
