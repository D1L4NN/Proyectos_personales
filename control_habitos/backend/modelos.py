from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

import datetime

class Habitos(Base):
    __tablename__ = "Habitos"
    id_habito = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    fecha_creado = Column(DateTime, default=datetime.datetime.utcnow)
    terminadas = relationship("HabitoTerminado", back_populates="habito", cascade="all, delete-orphan")

class HabitoTerminado(Base):
    __tablename__ = "habitos_terminados"
    id_terminado = Column(Integer, primary_key=True, index=True) 
    id_habito = Column(Integer, ForeignKey("Habitos.id_habito"))
    fecha_terminado = Column(Date, index = True)
    habito = relationship("Habitos", back_populates="terminadas")
