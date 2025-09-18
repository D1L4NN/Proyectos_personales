# este el el .py de las funciones de crud

from sqlalchemy.orm import Session
import modelos
from datetime import date, timedelta

def obtenerHabitos(db: Session):
    return db.query(modelos.Habitos).all()

def creaHabito(db: Session, nombre: str):
    # creo el habito
    habito = modelos.Habitos(nombre=nombre)
    # agrego el habito a la base de datos
    db.add(habito)
    # confirmo la agregada de habito
    db.commit()
    # refresco el registro ingresado/creado
    db.refresh(habito)
    # retorno el habito creado
    return habito

def obtenerHabitoPorId(db:Session, idHabito: int):
    # retorna el habito filtrado pr el parametro de su id 
    return db.query(modelos.Habitos).filter(modelos.Habitos.id_habito == idHabito).first()
def eliminaHabitoPorId(db: Session, idHabito: int):
    # obtenemos el habito mediante la funcion creada para obtenerlo mediante su id
    habito = obtenerHabitoPorId(db, idHabito)
    # si encuentra el habito, entonces es borrado
    if habito:
        db.delete(habito)
        db.commit() # confirmamos el borrado
        return True

def cambiaCompletado(db: Session, idHabito: int):
    hoy = date.today()
    # verificamos si el habito al que le querramos activar 
    # el completado existe en la tabla de los habitos terminados
    existente = db.query(modelos.HabitoTerminado).filter(
        modelos.HabitoTerminado.id_habito == idHabito,
        modelos.HabitoTerminado.fecha_terminado == hoy
    ).first()
    # Si exite se lo borra de esa tabla y se retorna "removido"
    if existente:
        db.delete(existente)
        db.commit() # confirmar 
        return {"cambiado": "removido"}
    else:
        habitoCompletado = modelos.HabitoTerminado(idHabito=idHabito, date= hoy)
        db.add(habitoCompletado)
        db.commit()
        db.refresh(habitoCompletado)
        return {"cambiado": "agregado"}
    
def obtieneProgreso(db: Session, dias: int = 7):
    inicio = date.today() - timedelta(dias=dias-1)
    complts = db.query(modelos.HabitoTerminado).filter(modelos.HabitoTerminado.fecha_terminado >= inicio).all()
    # inicializa un diccionario con 0 para cada dia
    contador = {}
    for i in range(dias):
        d = inicio + timedelta(dias=i)
        contador[d.isoformat()]=0
    for c in complts:
        contador[c.fecha_terminado.isoformat()] += 1
    # resultado como lista ordenada por fecha
    items = [{"fecha": k, "cuenta": contador[k]} for k in contador.keys()]
    return items
