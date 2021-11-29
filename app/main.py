from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.params import Depends
from starlette.responses import RedirectResponse 
from sqlalchemy.orm import Session
from . import models, schemas
from .conexion import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://127.0.0.1:5501"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url='/docs')

@app.get("/reservaciones/", response_model=List[schemas.Reserva], tags=["reservaciones"])
def show_reservas(db:Session = Depends(get_db)):
    reservaciones = db.query(models.Reserva).all()
    return reservaciones

@app.post("/reservaciones/", response_model=schemas.Reserva, tags=['reservaciones'])
def create_reservas(entrada:schemas.Reserva, db:Session = Depends(get_db)):
    reservacion = models.Reserva(
        nombre = entrada.nombre,
        apellido = entrada.apellido,
        fecha_reserva = entrada.fecha_reserva,
        telefono = entrada.telefono,
        personas = entrada.personas,
        comentarios = entrada.comentarios,
    )
    db.add(reservacion)
    db.commit()
    db.refresh(reservacion)
    return reservacion

@app.put("/reservaciones/{mesa_id}", response_model=schemas.Reserva, tags=['reservaciones'])
def update_reservas(mesa_id:int,entrada:schemas.Reserva, db:Session = Depends(get_db)):
    reservacion = db.query(models.Reserva).filter(models.Reserva.id == mesa_id).first()
    reservacion.nombre = entrada.nombre
    db.commit()
    db.refresh(reservacion)
    return reservacion

@app.delete("/reservaciones/{mesa_id}", response_model=schemas.Respuesta, tags=['reservaciones'])
def delete_reservas(mesa_id:int, db:Session = Depends(get_db)):
    reservacion = db.query(models.Reserva).filter(models.Reserva.id == mesa_id).first()
    db.delete(reservacion)
    db.commit()
    respuesta = schemas.Respuesta(mensaje = "Reservacion eliminada")
    return respuesta


##Ordenes

@app.get("/ordenes/", response_model=List[schemas.Orden], tags=["Ordenes"])
def show_ordenes(db:Session = Depends(get_db)):
    ordenes = db.query(models.Orden).all()
    return ordenes

@app.post("/Ordenes/", response_model=schemas.Orden, tags=['Ordenes'])
def create_orden(entrada:schemas.Orden, db:Session = Depends(get_db)):
    ordenes = models.Orden(
        pedido = entrada.pedido,
        cantidad = entrada.cantidad,
        total = entrada.total,
    )
    db.add(ordenes)
    db.commit()
    db.refresh(ordenes)
    return ordenes