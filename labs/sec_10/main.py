from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def get_db_version():
    try:
        # ket noi voi databse
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"message": "Ket noi ok", "db_version": db_version}
    except Exception as e:
        return {"message": "Loi ket noi voi DB", "error": str(e)}
