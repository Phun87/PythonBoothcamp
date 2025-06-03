import random
from art import logo

HARD_LEVEL = 5 #Global constant used when this number is fixed
EASY_LEVEL = 10

# Compare the answer
def compare(number, answer, turns):
    """This compare the user guess to the actual answer and returns the no of turns remaining"""
    if answer < number:
        print("Too Low")
        return turns - 1
    elif answer > number:
        print("Too high")
        return turns - 1
    else:
        print(f"You guessed it right. The number was {number}.")

# Set difficulty
def difficulty():
    """Returns the number of turns based on the difficulty level"""
    level = input("Choose the difficulty. Type 'hard' or 'easy'. ")
    if level == "hard":
        return HARD_LEVEL
    elif level == "easy":
        return EASY_LEVEL
    else:
        print("You have entered an invalid level.")
        exit()


def game():
    print(logo)
    print("Welcome to a number guessing game")
    print("I am thinking of a number between 1 and 100.")
    # Generate a random number
    computer_number = random.randint(1, 100)
    # print(computer_number)
    turns = difficulty()

    # Get the user input
    user_answer = 0 #Declare the variable so that it can be used in the while loop below
    while user_answer != computer_number:
        print(f"You have {turns} attempts left")
        user_answer = int(input("Guess the number: "))
        turns = compare(computer_number, user_answer, turns)
        # Track the level
        if turns == 0:
            print("You've run out of guesses. You Lose")
            break

game()


