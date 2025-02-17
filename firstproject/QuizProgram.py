import json


def load_questions():
    return [
        {"question": "What is the capital of France?", "options": ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
         "answer": "C"},
        {"question": "Which programming language is known for data science?",
         "options": ["A. Python", "B. Java", "C. C++", "D. Swift"], "answer": "A"},
        {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C. 15", "D. 20"], "answer": "B"},
    ]


def run_quiz():
    questions = load_questions()
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was", q["answer"])

    print(f"\nYour final score: {score}/{len(questions)}")
    retry = input("Do you want to retry the quiz? (yes/no): ").strip().lower()
    if retry == "yes":
        run_quiz()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    run_quiz()
