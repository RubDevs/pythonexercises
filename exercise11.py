# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
def consultar():
    number = int(input("Introduce un numero: "))
    return number


def es_primo():
    number = consultar()
    lista = range(2, (number/2)+1)
    a = [element for element in lista if number % element == 0]
    if len(a) == 0 and number != 1:
        print("Es un numero primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    es_primo()
