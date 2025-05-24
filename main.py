from fastapi import FastAPI

class Date:
    def __init__(self, hour, minute, day, month, year):
        self.hour = hour
        self.minute = minute
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.year}{self.month:02d}{self.day:02d}{self.hour:02d}{self.minute:02d}"
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d} de {self.day:02d}/{self.month:02d}/{self.year}"

class Appointment:
    def __init__(self, name: str, date: Date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"Tens de ir {self.name} às {str(self.date)}"
   
def date_size(appointment:Appointment):
    return int(repr(appointment.date))
    
appointments = [
    Appointment("Urologista", Date(23, 5, 3, 5, 2025)), 
    Appointment("Putas", Date(0, 0, 13, 12, 2025)),
    Appointment("Derrubar Império Romano", Date(13, 0, 1, 1, 2032)),
    Appointment("fazer sexo com o mesquita", Date(22, 0, 24, 5, 2025))
]

appointments.sort(key=date_size)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Loom"}

@app.get("/appointments/")
def see_appointments():
    return appointments

@app.get("/appointments/{appointment_id}")
def see_appointment(appointment_id: int):
    return str(appointments[appointment_id])


#  ⠀⠖⠖⡆⠀⠀⠀⠀⣀⣀⣀⠀⠀
#  ⢸⠀⠀⡗⠐⠉⠁⠀⠀⣇⡤⠽⡆
#  ⠀⢉⡟⠳⡄⠀⠀⠀⢀⣇⣀⡴⠃
#  ⠀⡏⠀⠀⡸⠉⠉⠉⠁⠀⠀⠀⠀ M + D