from fastapi import FastAPI
from app.routes import example

app = FastAPI(title="API Projeto com Pip")

app.include_router(example.router)

@app.get("/")
def root():
    return {"message": "API Online"}
