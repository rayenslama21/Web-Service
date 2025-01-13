from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random

app = FastAPI()


class TriviaQuestion(BaseModel):
    id: int
    exhibit_id: int
    question: str
    options: List[str]
    correct_answer: str
    difficulty: str  # e.g., 'easy', 'medium', 'hard'


class TriviaAnswer(BaseModel):
    username: str
    question_id: int
    answer: str

class TriviaAnsw(BaseModel):
    question_id: int
    answer: str

# Sample trivia database
trivia_db: List[TriviaQuestion] = [
    # (Add your questions here as in your existing database)

    TriviaQuestion(id=1, exhibit_id=1, question="What civilization influenced Carthaginian art the most?", options=["Greek", "Roman", "Phoenician", "Egyptian"], correct_answer="Phoenician", difficulty="easy"),
    TriviaQuestion(id=2, exhibit_id=1, question="What material was commonly used in Carthaginian sculptures?", options=["Bronze", "Marble", "Clay", "Wood"], correct_answer="Clay", difficulty="medium"),
    TriviaQuestion(id=3, exhibit_id=2, question="Where was the Bizerte Lake Mosaic discovered?", options=["Sousse", "Sidi Abdallah", "Carthage", "Bulla Regia"], correct_answer="Sidi Abdallah", difficulty="easy"),
    TriviaQuestion(id=4, exhibit_id=1, question="What materials were used to create the Bizerte Lake Mosaic?", options=["Clay and Marble", "Marble and Limestone", "Bronze and Limestone", "Marble and Wood"], correct_answer="Marble and Limestone", difficulty="medium"),
    TriviaQuestion(id=5, exhibit_id=1, question="What was the origin of the Julius Seigniorial Domain?", options=["Bulla Regia", "Carthage", "Sidi Abdallah", "Sousse"], correct_answer="Carthage", difficulty="easy"),
    TriviaQuestion(id=6, exhibit_id=1, question="What materials were used in the Julius Seigniorial Domain artifacts?", options=["Clay and Marble", "Marble and Wood", "Bronze and Clay", "Limestone and Clay"], correct_answer="Clay and Marble", difficulty="medium"),
    TriviaQuestion(id=7, exhibit_id=1, question="What verse of the Aeneid was Virgil writing in the 'Virgil and the Muses' mosaic?", options=["VIII", "V", "X", "VII"], correct_answer="VIII", difficulty="easy"),
    TriviaQuestion(id=8, exhibit_id=4, question="Where was the 'Virgil and the Muses' mosaic discovered?", options=["Carthage", "Sousse", "Bulla Regia", "Sidi Abdallah"], correct_answer="Sousse", difficulty="easy"),
    TriviaQuestion(id=9, exhibit_id=5, question="What was the origin of the Apollo Citharoedus statue?", options=["Sousse", "Bulla Regia", "Carthage", "Sidi Abdallah"], correct_answer="Bulla Regia", difficulty="easy"),
    TriviaQuestion(id=10, exhibit_id=5, question="Which mythical rival of Apollo is indirectly referenced in the Apollo Citharoedus statue?", options=["Marsyas", "Orpheus", "Dionysus", "Zeus"], correct_answer="Marsyas", difficulty="medium"),
]

# Dictionary to store user scores
scores: Dict[str, int] = {}


@app.get("/questions", response_model=List[TriviaQuestion])
def get_all_trivia_questions():
    """
    Retrieve all trivia questions.
    """
    return trivia_db


@app.get("/{exhibit_id}", response_model=List[TriviaQuestion])
def get_trivia_questions_for_exhibit(exhibit_id: int):
    """
    Retrieve trivia questions for a specific exhibit.
    """
    questions = [q for q in trivia_db if q.exhibit_id == exhibit_id]
    if not questions:
        raise HTTPException(status_code=404, detail="No trivia questions found for this exhibit.")
    return questions


@app.post("/answer")
def submit_trivia_answer(answer: TriviaAnswer):
    """
    Submit an answer to a trivia question and check correctness.
    """
    question = next((q for q in trivia_db if q.id == answer.question_id), None)
    if not question:
        raise HTTPException(status_code=404, detail="Trivia question not found.")
    
    # Initialize score if user doesn't exist
    if answer.username not in scores:
        scores[answer.username] = 0

    # Check correctness of the answer
    is_correct = question.correct_answer.lower() == answer.answer.lower()
    if is_correct:
        scores[answer.username] += 1  # Increment score for correct answer
    else:
        scores[answer.username] -= 1  # Decrement score for incorrect answer

    return {
        "question": question.question,
        "correct": is_correct,
        "correct_answer": question.correct_answer,
        "score": scores[answer.username],
    }


@app.get("/score/{username}")
def get_user_score(username: str):
    """
    Retrieve the score for a specific user.
    """
    if username not in scores:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"username": username, "score": scores[username]}


@app.post("/questions", response_model=TriviaQuestion)
def add_trivia_question(question: TriviaQuestion):
    """
    Add a new trivia question.
    """
    if any(q.id == question.id for q in trivia_db):
        raise HTTPException(status_code=400, detail="Question with this ID already exists.")
    trivia_db.append(question)
    return question


@app.get("/random/{exhibit_id}", response_model=TriviaQuestion)
def get_random_trivia_question(exhibit_id: int):
    """
    Get a random trivia question for a specific exhibit.
    """
    questions = [q for q in trivia_db if q.exhibit_id == exhibit_id]
    if not questions:
        raise HTTPException(status_code=404, detail="No trivia questions found for this exhibit.")
    return random.choice(questions)

@app.post("/answ")
def submit_trivia_answer(answer: TriviaAnsw):
    """
    Submit an answer to a trivia question and check correctness.
    """
    
    question = next((q for q in trivia_db if q.id == answer.question_id), None)
    if not question:
        raise HTTPException(status_code=404, detail="Trivia question not found.")
    
    
    is_correct = question.correct_answer.lower() == answer.answer.lower()

    return {
        "question": question.question,
        "correct": is_correct,
        "correct_answer": question.correct_answer,
    }
