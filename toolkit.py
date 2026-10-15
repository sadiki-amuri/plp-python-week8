# toolkit.py
import random

def play_guessing_game():
    """
    Tool 1: Number-Guessing Game.
    Uses a loop to keep requesting inputs, conditionals to check boundaries, 
    and f-strings for targeted feedback.
    """
    print("\n---  Tool 1: Number-Guessing Game ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    print("I am thinking of a number between 1 and 20. Can you find it?")

    while True:
        user_input = input("Enter your guess: ").strip()
        if not user_input.isdigit():
            print(" Invalid input. Please enter a valid number.")
            continue
            
        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print(f" Too low! Try a higher value. (Attempts: {attempts})")
        elif guess > secret_number:
            print(f" Too high! Try a lower value. (Attempts: {attempts})")
        else:
            print(f" Fantastic! You found the number {secret_number} in {attempts} attempts!")
            break

def manage_todo_list():
    """
    Tool 2: To-Do List Tracker.
    Maintains a list data structure that changes dynamically while running.
    Uses membership 'in' checking operators to prevent crash errors.
    """
    print("\n--- Tool 2: To-Do List Tracker ---")
    todos = []
    
    while True:
        print(f"\nCurrent Tasks: {todos if todos else 'No tasks logged yet!'}")
        action = input("Choose task operation (add / remove / show / back): ").strip().lower()

        if action == "add":
            task = input("Enter the new task: ").strip()
            if task:
                todos.append(task)
                print(f" Added task: '{task}'")
        elif action == "remove":
            task = input("Enter the exact task name to remove: ").strip()
            if task in todos:
                todos.remove(task)
                print(f" Removed task: '{task}'")
            else:
                print(f" '{task}' was not found in your list.")
        elif action == "show":
            print("\n--- Your Daily Checklist ---")
            for index, item in enumerate(todos, 1):
                print(f"{index}. {item}")
        elif action == "back":
            print("Exiting To-Do tracker module.")
            break
        else:
            print(" Command not recognized. Use add, remove, show, or back.")

def run_calculator():
    """
    Tool 3: Simple Calculator.
    Demonstrates clean arithmetic decision structures using conditionals.
    """
    print("\n---  Tool 3: Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(" Error: Invalid input parameters. Please use numbers only.")
        return

    operation = input("Choose an operator (+, -, *, /): ").strip()

    if operation == "+":
        print(f" Result: {num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f" Result: {num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f" Result: {num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print(" Error: Illegal division by zero.")
        else:
            print(f" Result: {num1} / {num2} = {num1 / num2}")
    else:
        print(" Unknown operator pattern selection.")

def main():
    """
    Main application hub. Handles the persistent menu loop shell, routing actions,
    and managing out-of-bounds menu entries safely.
    """
    print("==================================================")
    print(" Welcome to the PLP Python Multi-Tool Kit Engine")
    print("==================================================")

    while True:
        print("\n--- MAIN TOOLKIT MENU ---")
        print("1. Play Number-Guessing Game")
        print("2. Manage To-Do List Tracker")
        print("3. Open Simple Calculator")
        print("4. Quit Program")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            manage_todo_list()
        elif choice == "3":
            run_calculator()
        elif choice == "4":
            print("\n==================================================")
            print(" Thank you for using the Toolkit. Goodbye!")
            print("==================================================")
            break
        else:
            print(" Polite Notification: That selection is not on our menu. Please try again.")

if __name__ == "__main__":
    main()
