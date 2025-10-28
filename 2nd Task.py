import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    while True:
        choice = input("Select difficulty (Easy(1)-Hard(3)): ")
        if choice in ['1','2','3']:
            return int(choice)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(0, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    while True:
        try:
            answer = int(input(f"{num1} {operation} {num2} = "))
            return answer
        except ValueError:
            print("Please enter a valid integer.")

def isCorrect(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Good Job! :>\n")
        return True
    else:
        print("Wrong.  >:[")
        return False

def displayResults(score):
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

def playQuiz():
    difficulty = displayMenu()
    score = 0
    for i in range(1, 11):
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()
        correct_answer = num1 + num2 if operation == '+' else num1 - num2

        # First attempt
        user_answer = displayProblem(num1, num2, operation)
        if isCorrect(user_answer, correct_answer):
            score += 10
            continue

        # Second attempt
        print("Try again, i believe in you!")
        user_answer = displayProblem(num1, num2, operation)
        if isCorrect(user_answer, correct_answer):
            score += 5
        else:
            print(f"This is the correct answer: {correct_answer}\n")

    displayResults(score)

def main():
    print("Welcome to the Arithmetic Quiz!\n")
    while True:
        playQuiz()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for trying! :D")
            break
        print()

if __name__ == "__main__":
    main()