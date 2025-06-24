from fastapi import FastAPI
from app.routes.pedidos_routes import router as pedidos_router
from app.models.pedidos import Base
from app.database import engine

app = FastAPI()


@app.on_event("startup")
def startup():
    # Cria as tabelas no banco (se ainda não existirem)
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "ok"}


# Registra as rotas
app.include_router(pedidos_router)
