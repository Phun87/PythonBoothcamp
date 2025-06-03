from art import logo
import random

def draw_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compare the user score vs computer score"""
    if u_score == c_score:
        return "It's a draw"
    elif c_score == 0:
        return "Your opponent has a Blackjack. You lose!"
    elif u_score == 0:
        return "You win with a Blackjack"
    elif u_score > 21:
        return "You went over 21. You lose!"
    elif c_score >21:
        return "Your opponent went over 21. You win!"
    elif c_score > u_score:
        return "You lose!"
    else:
        return "You win!"

def play_game():
    print(logo)
    user_cards = []
    user_score = -1
    computer_cards = []
    computer_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(draw_cards())
        computer_cards.append(draw_cards())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and your current score: {user_score}")
        print(f"Your opponent's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_user_deal = input("Do you want to deal another cards? type 'Y' or 'N': ").lower()
            if should_user_deal == "y":
                user_cards.append(draw_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_cards())
        computer_score = calculate_score(computer_cards)
        print(f"Your final cards: {user_cards}, your final score: {user_score}")
        print(f"Your opponent's final cards: {computer_cards}, and your opponent's final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'Y' or 'N':").lower() == "y":
    print("\n" * 30)
    play_game()
