import datetime

# Ask user for his name and age and return a message with the year when user is going to be 100 years old.


def consultar_datos():
    nombre = input("Cual es tu nombre? ")
    edad = int(input("Cual es tu edad? "))
    printyear(nombre, edad)


def printyear(nombre, edad):
    actualyear = int(datetime.datetime.now().year)
    diffhudred = 100 - edad
    yearhundred = actualyear + diffhudred
    mensaje = "Hola " + nombre + \
        " cumpliras 100 anos en el " + str(yearhundred) + "\n"

    print(mensaje)
    times = int(input("Ingresa otro numero: "))
    print(mensaje*times)


if __name__ == '__main__':
    consultar_datos()
