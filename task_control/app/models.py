from sqlalchemy import Column, Integer, String, Boolean, DateTime
# Importando la varibable Base
from .database import Base
from datetime import datetime

# Creando clase para las tareas
class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    completado = Column(Boolean, default=False)
    fecha_limite = Column(DateTime, nullable=True)
    creado_en = Column(DateTime, default=datetime.utcnow)

