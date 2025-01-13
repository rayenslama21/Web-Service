from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel, EmailStr
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


tokens = {}


class ReservationRequest(BaseModel):
    name: str
    email: EmailStr


def send_token_email(name, email, token):
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "rayenslamaa@gmail.com"  
    sender_password = "easb ggda jjkc jkyw"  

    
    subject = "Museum Reservation Confirmation Token"
    body = f"""Dear {name},

Thank you for starting the reservation process.

Your confirmation token is: {token}

Please enter this token to confirm your reservation.

Best regards,
Museum Team"""

    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

   
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(sender_email, sender_password)
        server.send_message(msg)


@app.post("/reserve")
async def reserve_ticket(request: ReservationRequest):
    name = request.name
    email = request.email

    
    token = str(random.randint(100000, 999999))

    
    tokens[email] = token

    
    try:
        send_token_email(name, email, token)
        return {"message": "A confirmation token has been sent to your email."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send token email: {e}")


class ConfirmationRequest(BaseModel):
    email: EmailStr
    token: str

@app.post("/confirm")
async def confirm_reservation(request: ConfirmationRequest):
    email = request.email
    token = request.token

    if email in tokens and tokens[email] == token:
        del tokens[email] 
        return {"message": "Reservation confirmed! Thank you."}
    else:
        raise HTTPException(status_code=400, detail="Invalid token. Reservation not confirmed.")
