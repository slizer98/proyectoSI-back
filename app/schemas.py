from typing import Optional
from pydantic import BaseModel

class Reserva(BaseModel):
    id: Optional[int]
    nombre:  str  
    apellido: str  
    telefono: str  
    fecha_reserva: str  
    personas: int 
    comentarios: str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje: str


class Orden(BaseModel):
    id_orden: Optional[int]
    title: str
    precio: int

    class Config:
        orm_mode = True