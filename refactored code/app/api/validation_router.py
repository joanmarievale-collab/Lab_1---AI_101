# validation_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, validator

router = APIRouter()

class TextInput(BaseModel):
    text: str

    @validator("text")
    def must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Text input cannot be empty")
        return v

@router.post("/validate-text", tags=["Validation"])
async def validate_input(input: TextInput):
    return {"valid": True, "length": len(input.text)}
