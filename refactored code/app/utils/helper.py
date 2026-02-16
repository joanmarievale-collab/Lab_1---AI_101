# helper.py
from database import quiz_data, user_scores
from models.schemas import QuizResponse, Score

def get_all_questions():
    return [
        {
            "id": q["id"],
            "question": q["question"],
            "options": q["options"]
        }
        for q in quiz_data
    ]

def check_answer(response: QuizResponse) -> bool:
    for question in quiz_data:
        if question["id"] == response.question_id:
            return question["answer"].lower() == response.selected_option.lower()
    return False

def update_user_score(username: str, correct: bool):
    if username not in user_scores:
        user_scores[username] = 0
    if correct:
        user_scores[username] += 1
    return user_scores[username]

def get_user_score(username: str) -> int:
    return user_scores.get(username, 0)
