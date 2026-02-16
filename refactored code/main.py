# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.quiz_router import router as quiz_router
from routers.validation_router import router as validation_router
from routers.health_router import router as health_router
from utils.logger import setup_logger
from utils.security import verify_api_key
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

app = FastAPI(
    title="AI 101 Learning Lab API",
    description="Backend API for AI 101 Quiz and Validation Modules",
    version="1.0.0"
)

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API key middleware
@app.middleware("http")
async def check_api_key(request: Request, call_next):
    if request.url.path.startswith("/api"):
        api_key = request.headers.get("x-api-key")
        if not verify_api_key(api_key):
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
    response = await call_next(request)
    return response

# Routers
app.include_router(health_router, prefix="/health", tags=["Health Check"])
app.include_router(quiz_router, prefix="/api/quiz", tags=["Quiz"])
app.include_router(validation_router, prefix="/api/validate", tags=["Validation"])

# Initialize logger
setup_logger()
