from HigherOrLowerArt import logo, vs
from game_data import data
from random import randint

print(logo)


def calculateResult(a, b):
    if getFollowerCount(a) > getFollowerCount(b):
        return "Next round"
    else:
        return "Game over"


def getName(celeb):
    return celeb["name"]


def getDescription(celeb):
    return celeb["description"]


def getCountry(celeb):
    return celeb["country"]


def getFollowerCount(celeb):
    followers = celeb["follower_count"]
    return followers


def start_game():
    highScore = 0
    is_playing = True

    while is_playing:
        round = 1
        currentRandom = randint(0, len(data) - 1)
        againstRandom = randint(0, len(data) - 1)
        currentName = data[currentRandom]
        againstName = data[againstRandom]
        print(f"Round {round}")
        print(
            f"Compare A: {getName(currentName)}, {getDescription(currentName)}, from {getCountry(currentName)}"
        )
        print(vs)

        print(
            f"Against B: {getName(againstName)}, {getDescription(againstName)}, from {getCountry(againstName)}"
        )

        userGuess = input("Who has more followers: Type 'A' or 'B': ").capitalize()
        if result == "Game over":
            print(f"Game over, final score {highScore}")

            is_playing = False
        if userGuess == "A":
            result = calculateResult(currentName, againstName)
            highScore += 1

        elif userGuess == "B":
            result = calculateResult(againstName, currentName)
            highScore += 1


start_game()
