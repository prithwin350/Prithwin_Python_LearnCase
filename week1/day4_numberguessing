import random

def sum_of_even_numbers_game():
    print("Welcome to the Sum of Even Numbers Game!")
    print("Let's calculate the sum of even numbers up to a given number.\n")

    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Please enter a positive integer.\n")
            return
        if num >0:
            total = 0
            for i in range(1,num+1):
                if i%2==0:
                    total = total + i
            print(f"The sum of even numbers from 1 to {num} is: {total}\n")
            print("Going back to the menu.\n")

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.\n")

def multiplication_game():
    print("Welcome to the Multiplication Game!")
    print("Let's practice multiplication!\n")

    try:
        num = int(input("Enter the first number: "))
        for i in range(1, 11):
            result = num*i
            print(f"{num} x {i} = {result}")
        
        print("\nGoing back to the menu.\n")
    except:
        print("Invalid input. Please enter valid numbers.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    guess= random.randint(1, 100)
    attempts = 10
    while True:
        try:
            number=int(input("Enter your guess: "))
            attempts -= 1
            if number < guess:
                print("Too low! Try again.\n")
                print(f"You have {attempts} attempts left.\n")
            elif number > guess:
                print("Too high! Try again.\n")
                print(f"You have {attempts} attempts left.\n")
            elif number == guess:
                print(f"Congratulations! You've guessed the number {guess} in {attempts} attempts.\n")
                break
            if attempts == 0:
                print(f"Sorry, you've run out of attempts. The number was {guess}.\n")
                break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.\n")

def application():
    print("Initializing the Application...\n")
    while True:
        print("Choose a game to play:")
        print("1. Number Guessing Game")
        print("2. Multiplication")
        print("3. Sum of Even numbers")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            print("Starting the Number Guessing Game...\n")
            number_guessing_game()
        elif choice == 2:
            print("Starting the Multiplication Game...\n")
            multiplication_game()
        elif choice == 3:
            print("Starting the Sum of Even numbers Game...\n")
            sum_of_even_numbers_game()
        elif choice == 4:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.\n")
def main():
    print("Hello! Welcome to the Number games!\n")
    application()

main()