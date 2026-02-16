# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file if available

class Settings:
    PROJECT_NAME: str = "AI 101 Learning Lab"
    VERSION: str = "1.0.0"
    API_KEY: str = os.getenv("API_KEY", "ai101-secret-key")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
