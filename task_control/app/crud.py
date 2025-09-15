from sqlalchemy.orm import Session
# importo los archivos py de modelos y esquemas
from . import models,schemas

#
def obtener_tareas(db: Session):
    return db.query(models.Tarea).all()

def obtener_tarea(db: Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

# Funcion para crear una tarea
def crear_tarea(db: Session, tarea: schemas.TareaCreate):
    # creando una variable local que valide los datos de esquema
    db_tarea = models.Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def actualizar_tarea(db: Session, tarea_id: int, tarea_update: schemas.TareaUpdate):
    # Filtro la tarea por su id, recogiendo la tarea desde su clase de modelo con el id pasado por parametro
    # Ese id que evaluaremos lo guardaremos en la sigueinte variable
    tarea_db = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

    # Sin no encuentra el id, retorna nada
    if not tarea_db:
        return None
    
    # Setea los cambios para actualizar la tarea mediante funciones del esquema
    for key, value in tarea_update.dict(exclude_unset=True).items():
        setattr(tarea_db,key,value)

    db.commit()
    db.refresh(tarea_db)
    return tarea_db

def eliminar_tarea(db: Session, tarea_id: int):
    tarea_db = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

    if not tarea_db:
        return None
    
    db.delete(tarea_db)
    db.commit()
    return tarea_db

