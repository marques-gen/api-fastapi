import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "API Projeto com Pip"
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
