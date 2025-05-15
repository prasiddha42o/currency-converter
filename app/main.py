import logging
import sqlite3
from fastapi import FastAPI
from app.api.routes import router
from app.config import settings
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = settings.database_url

app = FastAPI()
app.include_router(router)


def init_db():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        """
                    CREATE TABLE IF NOT EXISTS conversions(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        from_currency TEXT NOT NULL,
                        to_currency TEXT NOT NULL,
                        amount REAL NOT NULL,    
                        converted_amount REAL NOT NULL,
                        rate REAL NOT NULL
                   )
                    """
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/")
def root():
    return {"message": "Welcome to the Currency Converter API!"}
