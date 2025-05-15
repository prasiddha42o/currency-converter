from fastapi import APIRouter, Depends
from app.models.currency import CurrencyConversion
from app.services.converter import convert_currency, get_history

router = APIRouter()


@router.post("/convert", response_model=CurrencyConversion)
def convert(amount: float, from_currency: str, to_currency: str):
    try:
        return convert_currency(amount, from_currency, to_currency)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/history")
def history():
    return get_history()
