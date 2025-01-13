from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import time
from virtual_visit import virtualvisit
from reservation import app as reservation_app
from fastapi.middleware.cors import CORSMiddleware
from exhibits import app as exhibits_app
from trivia import app as trivia_app
from winnersdb import app as winnersdb_app
from visitorsdb import app as visitors_app


app = FastAPI()


class WorkingHours(BaseModel):
    day: str
    open_time: time
    close_time: time


bardo_museum = {
    "name": "Bardo National Museum",
    "location": "Tunis in Mhammed Bey's Palace",
    "built": "Between 1859 and 1864",
    "working_hours": [
        {"day": "Monday", "open_time": "09:00", "close_time": "17:00"},
        {"day": "Tuesday", "open_time": "09:00", "close_time": "17:00"},
        {"day": "Wednesday", "open_time": "09:00", "close_time": "17:00"},
        {"day": "Thursday", "open_time": "09:00", "close_time": "17:00"},
        {"day": "Friday", "open_time": "09:00", "close_time": "17:00"},
    ],
}


@app.get("/museum/working-hours", response_model=List[WorkingHours])
def get_working_hours():
    """Retrieve the working hours of the Bardo National Museum."""
    return bardo_museum["working_hours"]

@app.put("/museum/working-hours", response_model=List[WorkingHours])
def update_working_hours(new_hours: List[WorkingHours]):
    """Update the working hours of the Bardo National Museum."""
    bardo_museum["working_hours"] = new_hours
    return bardo_museum["working_hours"]

@app.get("/museum/is-open", response_model=bool)
def is_open(day: str, current_time: time):
    """Check if the museum is open at a specific time on a specific day."""
    for hours in bardo_museum["working_hours"]:
        if hours["day"].lower() == day.lower():
            if hours["open_time"] <= current_time <= hours["close_time"]:
                return True
            return False
    raise HTTPException(status_code=404, detail="Day not found in working hours")


@app.post("/museum/working-hours/add", response_model=List[WorkingHours])
def add_working_hours(new_hours: WorkingHours):
    """Add new working hours for a specific day."""
    bardo_museum["working_hours"].append(new_hours.dict())
    return bardo_museum["working_hours"]


@app.delete("/museum/working-hours/delete")
def delete_working_hours(day: str):
    """Delete working hours for a specific day."""
    bardo_museum["working_hours"] = [hours for hours in bardo_museum["working_hours"] if hours["day"].lower() != day.lower()]
    return {"message": f"Working hours for {day} deleted successfully"}


@app.get("/museum/working-hours/{day}", response_model=WorkingHours)
def get_day_working_hours(day: str):
    """Get working hours for a specific day of the week."""
    for hours in bardo_museum["working_hours"]:
        if hours["day"].lower() == day.lower():
            return hours
    raise HTTPException(status_code=404, detail="Day not found in working hours")


app.include_router(virtualvisit, prefix="/museum", tags=["Virtual Visit"])

app.mount("/reservation", reservation_app)
app.mount("/exhibits", exhibits_app)
app.mount("/trivia", trivia_app)
app.mount("/visitors", visitors_app)
app.mount("/winners", winnersdb_app)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
