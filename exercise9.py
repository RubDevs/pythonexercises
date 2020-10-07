# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right.
import random


def jugar():
    number = random.randint(1, 9)
    usernumber = int(input("Adivina el numero (1-9): "))
    intentos = 0
    while True:
        if number == usernumber:
            intentos += 1
            print("Felicidades, acertaste ")
            print(f"Solo te tomo {intentos} intentos! ")
            salir = input("Quieres volver a jugar? y|n ")
            if salir in ('n', 'N'):
                break
            else:
                number = random.randint(1, 9)
                intentos = 0
                usernumber = int(input("Adivina el numero (1-9): "))
        elif (number < usernumber):
            intentos += 1
            if abs(number - usernumber) >= 4:
                print("Uyy estuviste muy lejos, baja mas ")
            elif abs(number - usernumber) < 4:
                print("Casi! baja un poco mas")
            usernumber = int(input("Adivina el numero (1-9): "))
        else:
            intentos += 1
            if abs(number - usernumber) >= 4:
                print("Uyy estuviste muy lejos, sube mas ")
            elif abs(number - usernumber) < 4:
                print("Casi! sube un poco mas")
            usernumber = int(input("Adivina el numero (1-9): "))


if __name__ == '__main__':
    jugar()
