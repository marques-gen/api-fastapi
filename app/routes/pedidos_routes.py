
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.pedidos import Pedido
from app.services.pedido_service import salvar_pedidos
from app.database import SessionLocal

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

# Injeta a sessão do banco


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def receber_pedidos(pedidos: List[Pedido], db: Session = Depends(get_db)):
    return salvar_pedidos(pedidos, db)
