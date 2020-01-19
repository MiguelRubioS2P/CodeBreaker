import random

def obtenerNumeroAleatorio():
    """
    Devolvemos un numero aleatorio, si no conseguimos crearlo aleatorio
    volvemos a llamar a la misma funcion
    :return:
    """
    numero1 = random.randint(0, 9)
    numero2 = random.randint(0, 9)
    numero3 = random.randint(0, 9)

    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        return obtenerNumeroAleatorio()
    else:
        resultado = str(numero1) + str(numero2) + str(numero3)

        return resultado

def comparar(numero1,numero2):
    """

    :param numero1: es un string
    :param numero2: es el numero que introducen
    :return:
    """
    if int(numero1) == numero2:
        return "Acertaste"
    else:
        # convertir el string numero1 en una lista para poder ordenarlo
        listaNumero1 = list(numero1)
        listaNumero1.sort()
        stringNumero2 = str(numero2)
        listaNumero2 = list(stringNumero2)
        listaNumero2.sort()
        if listaNumero1 == listaNumero2:
            return "Cerca"
        else:
            return "No"

def game():
    acertado = False
    # numero = obtenerNumeroAleatorio()
    numero = "023"
    try:
        pregunta = int(input("Di un numero de tres digitos \n"))
        respuesta = comparar(numero, pregunta)
        if respuesta == "Acertaste":
            acertado = True
        print respuesta
        print numero
    except:
        print "No se puede introducir un valor que sea distinto a un numero"

    while not (acertado):
        try:
            pregunta = int(input("Di un numero de tres digitos \n"))
            respuesta = comparar(numero, pregunta)
            if respuesta == "Acertaste":
                acertado = True
            print respuesta
            print numero
        except:
            print "No se puede introducir un valor que sea distinto a un numero"