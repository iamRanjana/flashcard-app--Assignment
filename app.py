from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# In-memory list of flashcards
flashcards = []

# ✅ Home route
@app.route('/', methods=['GET'])
def home():
    return "Smart Flashcard Backend Running Successfully!"

# ✅ Task 1: Add Flashcard
@app.route('/flashcard', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    flashcard = {
        'student_id': data['student_id'],
        'subject': data['subject'],
        'question': data['question'],
        'answer': data['answer']
    }
    flashcards.append(flashcard)
    return jsonify({'message': 'Flashcard added successfully', 'subject': flashcard['subject']}), 201

# ✅ Task 2: Get flashcards from different subjects (mixed)
@app.route('/get-subject', methods=['GET'])
def get_flashcards_by_subject():
    student_id = request.args.get('student_id')
    limit = int(request.args.get('limit', 5))

    # 1. Filter only flashcards for this student
    student_flashcards = [f for f in flashcards if f['student_id'] == student_id]

    # 2. Shuffle to mix order
    random.shuffle(student_flashcards)

    # 3. Pick up to 'limit' flashcards from different subjects
    seen_subjects = set()
    selected_flashcards = []
    for f in student_flashcards:
        if f['subject'] not in seen_subjects:
            selected_flashcards.append({
                "question": f['question'],
                "answer": f['answer'],
                "subject": f['subject']
            })
            seen_subjects.add(f['subject'])
        if len(selected_flashcards) == limit:
            break

    return jsonify(selected_flashcards)

# ✅ Optional: Get all flashcards by a specific subject (extra endpoint if needed)
@app.route('/get-by-subject', methods=['GET'])
def get_by_subject():
    student_id = request.args.get('student_id')
    subject = request.args.get('subject')
    result = [f for f in flashcards if f['student_id'] == student_id and f['subject'] == subject]
    return jsonify(result)

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)
