# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
import random


def generateNumber():
    return random.randint(1000, 9999)


def verify(rand_number, user_number):
    cows = 0
    bulls = 0
    for index in range(4):
        if user_number[index] == rand_number[index]:
            cows += 1
        if user_number[index] in rand_number:
            bulls += 1
    return cows, bulls-cows


def jugar():
    guesses = 0
    number = str(generateNumber())
    print("Welcome to the Cows and Bulls Game!")
    user_number = input("Enter a 4 digits number: ")
    cows, bulls = verify(number, user_number)
    while cows != 4:
        guesses += 1
        print(f"{cows} cows, {bulls}  bulls")
        user_number = input("Enter a 4 digits number: ")
        cows, bulls = verify(number, user_number)
    print(f"Te tomo {guesses} intentos")


if __name__ == "__main__":
    jugar()
