# Online Quiz Management System

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Hyderabad", "B. Delhi", "C. Mumbai", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. All of these"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Computer Personal Unit",
                    "C. Central Processing Unit", "D. Control Processing Unit"],
        "answer": "C"
    }
]

score = 0

print("----- Welcome to Online Quiz -----\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("Quiz Completed!")
print("Your Score:", score, "/", len(questions))