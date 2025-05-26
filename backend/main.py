from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    name: str
    date: datetime
    notes: str | None = None

    def __str__(self):
        return f"Tens de ir {self.name} às {self.date.strftime('%H:%M')} a {self.date.strftime('%d/%m/%Y')}"
      
appointments = [
    Appointment(name="Urologista", date=datetime(2025, 5, 3, 23, 5)), 
    Appointment(name="Putas", date=datetime(2025, 12, 13, 0, 0)),
    Appointment(name="Derrubar Império Romano", date=datetime(2032, 1, 1, 13, 0)),
    Appointment(name="fazer sexo com o mesquita", date=datetime(2025, 5, 24, 22, 0))
]

def sort_appointments():
    def date_size(appointment:Appointment):
        return appointment.date
    appointments.sort(key=date_size)
sort_appointments()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Loom"}

@app.get("/appointments/")
def see_appointments():
    return appointments

@app.get("/appointments/{appointment_id}")
def see_appointment(appointment_id  : int):
    return str(appointments[appointment_id])

@app.post("/appointments/")
async def create_appointment(appointment: Appointment):
    appointments.append(appointment)
    sort_appointments()
    return "POST BEM SUCEDIDO"

#  ⠀⠖⠖⡆⠀⠀⠀⠀⣀⣀⣀⠀⠀
#  ⢸⠀⠀⡗⠐⠉⠁⠀⠀⣇⡤⠽⡆
#  ⠀⢉⡟⠳⡄⠀⠀⠀⢀⣇⣀⡴⠃
#  ⠀⡏⠀⠀⡸⠉⠉⠉⠁⠀⠀⠀⠀ M + D