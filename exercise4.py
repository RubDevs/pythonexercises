# Ask the user for a number and then print a list of all numbers that divides evenly the given number


def consultar():
    number = int(input("Introduce un numero: "))
    list = [num for num in range(1, (number//2)+1) if number % num == 0]
    list.append(number)
    print(list)


if __name__ == "__main__":
    consultar()
