# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    id: int
    question: str
    options: List[str]

class QuizResponse(BaseModel):
    question_id: int
    selected_option: str

class Score(BaseModel):
    username: str
    score: int

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
