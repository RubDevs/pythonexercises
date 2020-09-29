a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# List Comprehension
b = [number for number in a if number < 21]

# Iterative way
for element in a:
    if element < 5:
        b.append(element)

print(b)


def consultar():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    numero = int(input("Introduce un numero: "))
    b = [number for number in a if number < numero]
    print(b)


if __name__ == "__main__":
    consultar()
