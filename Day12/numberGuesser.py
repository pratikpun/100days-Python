import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def check_answer(user_guess, computer_guess, turns):
    if user_guess > computer_guess:
        # reduce_life()
        print("Too high.")
        return turns - 1
    elif user_guess < computer_guess:
        # reduce_life()
        print("Too low.")
        return turns - 1
    else:
        print(f"You win!! The answer was {computer_guess}")


def start_game():
    print("Welcome to the Numberuser_ Guessing Game!")

    print("I'm thinking of a number between 1 and 100")

    computer_guess = random.randint(1, 100)

    print(f"hint: it's {computer_guess}")

    turns = set_difficulty()

    user_guess = 0
    while user_guess != computer_guess:
        print(f"You have {turns} attempts remaining to guess the number.")

        user_guess = int(input("Make a guess: "))

        turns = check_answer(user_guess, computer_guess, turns)
        if turns == 0:
            print(
                f"You've run out of guesses, you lose . . . The answer was {computer_guess}."
            )
            return
        elif user_guess != computer_guess:
            print("Guess again.")


start_game()
