from HigherOrLowerArt import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they are correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True


account_b = random.choice(data)  # Make the game repeateable
while game_should_continue:
    # Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final score: {score}")


# Make account at position B become the next account at position A
