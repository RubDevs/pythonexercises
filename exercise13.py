# Write a program that asks the user how many Fibonnaci numbers to generate
# and then generates them

def gen_fib(number):
    i = 1
    if number == 0:
        fib = []
    elif number == 1:
        fib = [1]
    elif number == 2:
        fib = [1, 1]
    elif number > 2:
        fib = [1, 1]
        while i < (number - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib


if __name__ == "__main__":
    numero = int(input("Cuantos numero de Fibonacci quieres? "))
    print(gen_fib(numero))
