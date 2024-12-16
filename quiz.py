import json
import random
import time

# Object-Oriented Programming (OOP) questions
oop_questions = [
    {"question": "What is encapsulation in OOP?", "options": ["Hiding implementation details", "Inheritance", "Polymorphism", "Abstraction"], "answer": 0},
    {"question": "Which feature allows one class to derive properties of another class?", "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], "answer": 1},
    {"question": "What is polymorphism in OOP?", "options": ["Overloading and Overriding", "Encapsulation", "Data hiding", "None of the above"], "answer": 0},
    {"question": "Which OOP principle focuses on exposing only essential details?", "options": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"], "answer": 1},
    {"question": "What is an object in OOP?", "options": ["A blueprint", "An instance of a class", "A function", "A variable"], "answer": 1},
    {"question": "What does 'self' refer to in Python classes?", "options": ["A global variable", "The instance of the class", "A parent class", "A static method"], "answer": 1},
    {"question": "Which OOP principle allows using the same function name for different purposes?", "options": ["Polymorphism", "Abstraction", "Encapsulation", "Inheritance"], "answer": 0},
    {"question": "Which keyword is used to define a class in Python?", "options": ["object", "class", "def", "new"], "answer": 1},
    {"question": "What is the purpose of a constructor in OOP?", "options": ["To initialize an object", "To destroy an object", "To overload methods", "None of the above"], "answer": 0},
    {"question": "Which of the following is not a pillar of OOP?", "options": ["Encapsulation", "Abstraction", "Polymorphism", "Compilation"], "answer": 3}
]

def register_player():
    print("Welcome to the Quiz Game!")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    print(f"Hello {name}, get ready to start the quiz!\n")
    return name

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    start_time = time.time()
    while True:
        try:
            answer = int(input("Enter the option number: ")) - 1
            if answer < 0 or answer >= len(options):
                raise ValueError("Invalid option. Please choose a valid option.")
            break
        except ValueError as e:
            print(e)
    end_time = time.time()
    
    if end_time - start_time > 30:  # Example timer of 30 seconds
        print("Time's up! Moving to the next question.\n")
        return 0

    return 1 if answer == correct_option else 0

def run_quiz(questions):
    score = 0
    selected_questions = random.sample(questions, 5)  # Select 5 random questions
    for question_data in selected_questions:
        print("\n-------------------\n")
        score += ask_question(
            question_data['question'], 
            question_data['options'], 
            question_data['answer']
        )
    return score

def display_score(player_name, score, total):
    print("\n===================")
    print(f"Quiz Over!\n{player_name}, your final score is {score} out of {total}.")
    print("===================")

if __name__ == "__main__":
    player_name = register_player()
    total_questions = 5
    final_score = run_quiz(oop_questions)
    display_score(player_name, final_score, total_questions)
