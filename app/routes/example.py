from fastapi import APIRouter

router = APIRouter(prefix="/example", tags=["Exemplo"])

@router.get("/")
def exemplo():
    return {"mensagem": "Rota de exemplo funcionando"}
