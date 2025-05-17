# Smart Flashcard App

This is a simple Flask app to manage flashcards by student and subject.

## Installation

```bash
pip install -r requirements.txt
python app.py

API Endpoints
1. Add Flashcard (POST)
Endpoint: /flashcard

Request Body (JSON):
{
  "student_id": "stu001",
  "subject": "Physics",
  "question": "What is Newton's First Law?",
  "answer": "An object in motion stays in motion unless acted upon."
}
Response:
{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}


2. Get Flashcards by Mixed Subjects (GET)
Endpoint: /get-subject?student_id=stu001&limit=3

Response: Returns up to limit flashcards from different subjects for the specified student, shuffled.

Example response:
[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  },
  {
    "question": "What is photosynthesis?",
    "answer": "A process used by plants to convert light into energy",
    "subject": "Biology"
  }
]

3. Get Flashcards by Specific Subject (GET)
Endpoint: /get-by-subject?student_id=stu001&subject=Physics

Response: Returns all flashcards for the specified student and subject.

Example response:
[
  {
    "student_id": "stu001",
    "subject": "Physics",
    "question": "What is Newton's First Law?",
    "answer": "An object in motion stays in motion unless acted upon."
  }
]

