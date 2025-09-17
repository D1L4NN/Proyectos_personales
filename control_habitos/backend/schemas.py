from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class HabitCreate(BaseModel):
    nombre: str

class HabitOut(BaseModel):
    id: int
    nombre: str
    creado_el: datetime
    completo_hoy: bool

    class Config:
        orm_mode = True

class ProgressItem(BaseModel):
    fecha: date
    contador: int