FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
#Copiar o restante da aplicação
COPY . .

EXPOSE 8000

# Define PYTHONPATH corretamente (opcional — prioridade é do docker-compose/devcontainer.json)
ENV PYTHONPATH=/workspaces/API-FASTAPI-TEMPLATE

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

