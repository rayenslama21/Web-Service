from fastapi import FastAPI, HTTPException
import mysql.connector
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Database configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "museum_db"


# Pydantic model for Visitors
class Visitor(BaseModel):
    id: int
    name: str
    email: str
    country: str
    reservation_code: str


@app.get("/visitors", response_model=List[Visitor])
def get_all_visitors():
    """
    Fetch all visitors from the database.
    """
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor(dictionary=True)

        # SQL query to fetch all visitors
        cursor.execute("SELECT id, name, email, country, reservation_code FROM visitors")
        visitors = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        # Return the list of visitors
        return visitors

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database error: {str(err)}")
