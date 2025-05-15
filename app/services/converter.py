import sqlite3
import httpx
from app.models.currency import CurrencyConversion
from app.config import settings

DATABASE_URL = settings.database_url
EXCHANGE_API_KEY = settings.exchange_api_key
EXCHANGE_API_URL = (
    "https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
)


def fetch_conversion_rate(from_currency: str, to_currency: str) -> float:
    if not EXCHANGE_API_KEY:
        raise RuntimeError("EXCHANGE_API_KEY not set")
    url = EXCHANGE_API_URL.format(
        api_key=EXCHANGE_API_KEY,
        from_currency=from_currency.upper(),
        to_currency=to_currency.upper(),
    )
    response = httpx.get(url)
    data = response.json()
    if data.get("result") != "success":
        raise ValueError("Exchange rate not available")
    return data["conversion_rate"]


def convert_currency(
    amount: float, from_currency: str, to_currency: str
) -> CurrencyConversion:
    rate = fetch_conversion_rate(from_currency, to_currency)
    converted_amount = amount * rate
    # Store in DB
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conversions (from_currency, to_currency, amount, converted_amount, rate) VALUES (?, ?, ?, ?, ?)",
        (from_currency.upper(), to_currency.upper(), amount, converted_amount, rate),
    )
    conn.commit()
    conn.close()
    return CurrencyConversion(
        from_currency=from_currency.upper(),
        to_currency=to_currency.upper(),
        amount=amount,
        converted_amount=converted_amount,
        rate=rate,
    )


def get_history():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT from_currency, to_currency, amount, converted_amount, rate FROM conversions"
    )
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "from_currency": row[0],
            "to_currency": row[1],
            "amount": row[2],
            "converted_amount": row[3],
            "rate": row[4],
        }
        for row in rows
    ]
