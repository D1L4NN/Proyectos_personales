from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional

class HabitCreate(BaseModel):
    nombre: str

class HabitOut(BaseModel):
    id: int =  Field(alias="id")
    nombre: str = Field(alias="name")
    creado_el: datetime = Field(alias="created_at")
    completo_hoy: bool = Field(alias="completed_today")
    class Config:
        populate_by_name = True
        orm_mode = True

class ProgressItem(BaseModel):
    fecha: date
    contador: int