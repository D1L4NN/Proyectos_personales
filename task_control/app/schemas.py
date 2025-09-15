from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Creando clase de esquema para tarea
class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    fecha_limite: Optional[datetime] = None

# Esquema para creacion de tarea
class TareaCreate(BaseModel):
    pass

# Esquema para actualizacion de tarea 
class TareaUpdate(BaseModel):
    completado: Optional[bool] = None

# Esquema para tarea 
class TareaOut(BaseModel):
    id: int
    completado: bool
    creado_en: datetime

    class config: 
        orm_mode: True



