from fastapi import FastAPI, HTTPException
import mysql.connector
from typing import List

app = FastAPI()

# Database configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "museum_db"

# Winner model
class Winner:
    def __init__(self, id, name, reservation, created_at):
        self.id = id
        self.name = name
        self.reservation = reservation
        self.created_at = created_at

# Endpoint to retrieve all winners
@app.get("/winners")
def get_all_winners():
    """
    Retrieve all winners from the winners table in the database.
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

        # Query all winners
        cursor.execute("SELECT * FROM winner")
        winners = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        # Return winners as JSON
        return {"winners": winners}

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
