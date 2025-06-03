from game_data import data
import random

def format_name(account):
    """Takes the account data and returns in printable format"""
    account_name = account["name"]
    account_country = account["country"]
    return f"{account_name} from {account_country}"

def check_answer(user_guess, follower_count_a, follower_count_b):
    """Takes the user guess and follower count and returns if they got it right"""
    if follower_count_a > follower_count_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_name(account_a)}")
    print("\n VS \n")
    print(f"Against B: {format_name(account_b)}")

    guess = input("Who has more followers on Instagram? Type 'A' or 'B' ").lower()
    print("\n" * 20)
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You got it right. Your current score is: {score}")
    else:
        print(f"You got it wrong. Your final score is {score}")
        game_should_continue = False
