from typing import List
from sqlalchemy.orm import Session
from app.models.pedidos import Pedido, PedidoORM
from datetime import datetime


def salvar_pedidos(pedidos: List[Pedido], db: Session) -> dict:
    total = len(pedidos)
    atrasados = [p for p in pedidos if p.Status_Pedido.lower() == "atrasado"]

    for p in pedidos:
        pedido = PedidoORM(
            ID_Pedido=p.ID_Pedido,
            Data_Pedido=datetime.strptime(p.Data_Pedido, "%Y-%m-%d").date(),
            Prazo_Entrega_Dias=p.Prazo_Entrega_Dias,
            Tempo_Transito_Dias=p.Tempo_Transito_Dias,
            Data_Entrega=datetime.strptime(p.Data_Entrega, "%Y-%m-%d").date(),
            Regiao=p.Regiao,
            Transportadora=p.Transportadora,
            Status_Pedido=p.Status_Pedido,
            Avaliacao_Cliente=p.Avaliacao_Cliente
        )
        db.add(pedido)

    db.commit()

    return {
        "mensagem": "Dados inseridos com sucesso.",
        "total_pedidos": total,
        "pedidos_atrasados": len(atrasados)
    }
