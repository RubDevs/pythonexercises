def consultar():
    number = int(input("Escribe un numero: "))
    mensaje = "es par" if number % 2 == 0 else "Es non"
    mensajefour = "Es multiplo de 4" if number % 4 == 0 else ""
    if len(mensajefour) > 0:
        print(mensajefour)
        segundaconsulta(number)
        return
    print(mensaje)
    segundaconsulta(number)


def segundaconsulta(number):
    numero = int(input("Ingresa otro numero: "))
    if numero % number == 0:
        print("Es multiplo de " + str(number))
    else:
        print("No es multiplo de " + str(number))


if __name__ == "__main__":
    consultar()
