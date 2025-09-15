from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Definiendo la url de la base de datos sqlite
DATABASE_URL = "sqlite:///./tareas.db"

# crando una variable instanciadora de create_engine
engine = create_engine(
    DATABASE_URL, connect_args = {"check_same_thread":False}
)

# Creando variable de sesion local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Variable de base 
Base = declarative_base()