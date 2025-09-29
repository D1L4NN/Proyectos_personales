from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, init_db

import modelos, schemas, crud
from datetime import date
from typing import List

# crea la base de datos y las tablas
init_db()

# creo la apu del control de habitos
app = FastAPI(title="API Control de habitos")

# permitir request desde Vite dev server (puerto 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers  = ["*"],
)

# dependencia
def obtieneDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/salud")
def salud():
    return {"status": "ok"}

@app.get("/habitos", response_model=List[schemas.HabitOut])
def leer_habitos(db: Session = Depends(obtieneDB)):
    habitos = crud.obtenerHabitos(db)
    hoy = date.today()
    out = []
    for h in habitos:
        completado_hoy = db.query(modelos.HabitoTerminado).filter_by(id_habito=h.id_habito, fecha_terminado=hoy).first() is not None
        out.append({
            "id": h.id_habito,
            "name": h.nombre,
            "created_at": h.fecha_creado,
            "completed_today": completado_hoy
        })
    return out



@app.post("/habitos", response_model=schemas.HabitOut)
def crear_habito(habito: schemas.HabitCreate, db: Session = Depends(obtieneDB)):
    h = crud.creaHabito(db, habito.nombre)
    return {
        "id": h.id_habito,
        "nombre": h.nombre,
        "creado_el": h.fecha_creado,
        "completo_hoy": False
    }


@app.post("/habitos/{id_habito}/completo")
def cambia_completado(id_habito: int, db: Session = Depends(obtieneDB)):
    if crud.obtenerHabitoPorId(db, id_habito) is None:
        raise HTTPException(status_code=404, detail="Habito no encontrado")
    return crud.cambiaCompletado(db, id_habito)


@app.delete("/habitos/{id_habito}")
def elimina_habito(id_habito: int, db: Session = Depends(obtieneDB)):
    ok = crud.eliminaHabitoPorId(db, id_habito)
    if not ok:
        raise HTTPException(status_code=404, detail="Habito no encontrado")
    return {"ok": True}


@app.get("/progreso")
def progreso(dias: int = 7, db: Session = Depends(obtieneDB)):
    items = crud.obtieneProgreso(db, dias)
    # retorna [{ "date": "2025-09-10", "count": 2 }, ...]
    return items