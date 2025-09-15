from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas,crud,database

models.Base.metadata.create_all(bind=database.engine)

#Creo variable instanciadora de FastAPI
app = FastAPI()

#Creo un endopoint para el enlace prinicipal
@app.get("/")
def read_root():
    return {"message:": "Hola, esto es FastAPI"}

#Dependencia
def get_db():
    db = database.SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.post("/tareas/", response_model=schemas.TareaOut)
def crear(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    return crud.crear_tarea(db,tarea)

@app.get("/tareas/", response_model=list[schemas.TareaOut])
def listar(db: Session=Depends(get_db)):
    return crud.obtener_tareas(db)

@app.get("/tareas/{tarea_id}", response_model=schemas.TareaOut)
def obtener(tarea_id: int, db: Session=Depends(get_db)):
    tarea = crud.obtener_tarea(db,tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada.")
    return tarea

@app.put("/tareas/{tarea_id}", response_model=schemas.TareaOut)
def actuaizar(tarea_id: int, tarea_update = schemas.TareaUpdate, db: Session= Depends(get_db)):
    tarea = crud.actualizar_tarea(db,tarea_id,tarea_update)
    if tarea is None:
        raise HTTPException(status_code=404, detail="No se encontró la tarea. Tarea no actualizada.")
    return tarea

@app.delete("/tareas/{tarea_id}", response_model= schemas.TareaOut)
def eliminar(tarea_id: int, db: Session=Depends(get_db)):
    tarea = crud.eliminar_tarea(db,tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detaill="No se eliminó la tarea. Tarea no encontrada")
    
    return tarea
