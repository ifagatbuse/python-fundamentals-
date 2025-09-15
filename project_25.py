# Project 25: Quiz Game
# Topic: Dictionary + input loop + scoring

questions = {
    "What is the capital of France? ": "paris",
    "2 + 2 = ? ": "4",
    "What color is the sky on a clear day? ": "blue"
}

score = 0
print("Welcome to the Quiz! Type your answer.\n")

for q, correct in questions.items():
    user = input(q).strip().lower()
    if user == correct:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong ❌  (Answer: {correct})")

print(f"\nFinal Score: {score} / {len(questions)}")
