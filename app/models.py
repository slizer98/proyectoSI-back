from sqlalchemy import Column, Integer, String
from .conexion import Base

class Reserva(Base):
    __tablename__ = 'reserva'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40))
    apellido = Column(String(40))
    telefono = Column(String(15))
    fecha_reserva = Column(String(20))
    personas = Column(Integer)
    comentarios = Column(String(100))


class Orden(Base):
    __tablename__ = 'ordenes'
    id_orden = Column(Integer, primary_key=True)
    pedido = Column(String(400))
    cantidad = Column(Integer)
    total = Column(Integer)