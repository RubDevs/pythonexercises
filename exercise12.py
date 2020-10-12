# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
import random


def random_list(size=5):
    return random.sample(range(1, 20), size)


def list_first_and_last(lista):
    return lista[:: len(lista)-1]


if __name__ == "__main__":
    lista = random_list(10)
    print(lista)
    print(list_first_and_last(lista))
