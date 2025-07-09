# ======================================================
#  Simple Blackjack Game (Python CLI)
#  I LEARNT THIS CODE FROM A COURSE 100 DAYS OF PYTHON BY DR. ANGELA
# ======================================================
# TODO 1: Import required modules
import random
from art2 import logo  # Make sure you have art2.py or a logo variable

# ======================================================
# TODO 2: Define function to deal a random card
def deal_card():
    """
    Returns a random card from the deck.
    Note: Ace = 11, Face cards = 10
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# ======================================================
# TODO 3: Define function to calculate the score
def calculate_score(cards):
    """
    Takes a list of cards and returns the score.
    Special rule: Blackjack is 0. If there's an Ace and score > 21, Ace = 1.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack!

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# ======================================================
# TODO 4: Define function to compare scores
def compare(user_score, computer_score):
    """
    Compares user score and computer score.
    Returns result as a string.
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# ======================================================
# TODO 5: Define function to play a single game round
def play_game():
    print(logo)  # ASCII art logo

    # Step 1: Initialize hands
    user_cards = []
    computer_cards = []

    # Step 2: Deal two cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    # Step 3: User turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Step 4: Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Step 5: Final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# ======================================================
# TODO 6: Game Loop to allow multiple rounds
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # Clear screen effect
    play_game()
