"""
Arithmetic Quiz Game
Rearranged version with comments for clarity.
"""
import random

# Display the menu and get difficulty level from user
def display_menu():
    print("DIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")

    while True:
        choice = input("Select difficulty (Easy(1)-Hard(3)): ")
        # Validate user input
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid input. Please enter 1, 2, or 3.")

# Generate random integer based on difficulty level
def random_int(difficulty):
    if difficulty == 1:
        return random.randint(0, 9)       # Easy: 0-9
    elif difficulty == 2:
        return random.randint(10, 99)     # Moderate: 10-99
    else:
        return random.randint(1000, 9999) # Advanced: 1000-9999

# Randomly choose + or -
def choose_operation():
    return random.choice(['+', '-'])

# Ask user for answer until valid input is given
def ask_question(num1, num2, operation):
    while True:
        try:
            return int(input(f"{num1} {operation} {num2} = "))
        except ValueError:
            print("Please enter a valid integer.")

# Check if answer is correct
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Good Job! :>\n")
        return True
    print("Wrong.  >:[")
    return False

# Display final score and grade
def show_results(score):
    print(f"Your final score: {score}/100")

    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    elif score > 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Your grade is {grade}\n")

# Main quiz logic
def play_quiz():
    difficulty = display_menu()
    score = 0

    for question in range(1, 11):
        num1 = random_int(difficulty)
        num2 = random_int(difficulty)
        operation = choose_operation()
        correct_answer = num1 + num2 if operation == '+' else num1 - num2

        # First attempt
        user_answer = ask_question(num1, num2, operation)
        if check_answer(user_answer, correct_answer):
            score += 10
            continue

        # Second attempt
        print("Try again, I believe in you!")
        user_answer = ask_question(num1, num2, operation)

        if check_answer(user_answer, correct_answer):
            score += 5
        else:
            print(f"This is the correct answer: {correct_answer}\n")

    show_results(score)

# Game entry point
def main():
    print("Welcome to the Arithmetic Quiz!\n")

    while True:
        play_quiz()
        again = input("Do you want to play again? (y/n): ").lower()

        if again != 'y':
            print("Thanks for trying! :D")
            break
        print()

# Run game
if __name__ == "__main__":
    main()
