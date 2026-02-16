# security.py
from fastapi import Header, HTTPException, status

API_KEY = "ai101-secret-key"  # Replace with env var or secrets manager in prod

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
