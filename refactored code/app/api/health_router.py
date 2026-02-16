# health_router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "AI 101 API is healthy"}
