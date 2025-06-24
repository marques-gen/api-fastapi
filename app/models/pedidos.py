from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Modelo ORM para banco


class PedidoORM(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ID_Pedido = Column(String)
    Data_Pedido = Column(Date)
    Prazo_Entrega_Dias = Column(Integer)
    Tempo_Transito_Dias = Column(Integer)
    Data_Entrega = Column(Date)
    Regiao = Column(String)
    Transportadora = Column(String)
    Status_Pedido = Column(String)
    Avaliacao_Cliente = Column(Integer)

# Modelo de entrada (validação)


class Pedido(BaseModel):
    ID_Pedido: str
    Data_Pedido: str
    Prazo_Entrega_Dias: int
    Tempo_Transito_Dias: int
    Data_Entrega: str
    Regiao: str
    Transportadora: str
    Status_Pedido: str
    Avaliacao_Cliente: int


""" class Pedido(BaseModel):
    ID_Pedido: str
    Data_Pedido: str
    Prazo_Entrega_Dias: float
    Tempo_Transito_Dias: float
    Data_Entrega: str
    Regiao: str
    Transportadora: str
    Status_Pedido: str
    Avaliacao_Cliente: float
 """
