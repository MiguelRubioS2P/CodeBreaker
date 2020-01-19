import random

def palabraAleatoria():
    """
    En este metodo tenemos una lista de valores, y generando un numero aleatorio devolvemos un
    valor de esa lista
    :return:
    """
    listaPalabras = ["cinco","migue","marta","jorge","yosua"]
    numero = random.randint(0, len(listaPalabras)-1)
    return listaPalabras[numero]



def compararPalabras(palabraIntroducida,palabraGenerada):
    auxiliar = ""
    if(len(palabraIntroducida) > 5):
        return "Tiene mas de 5 caracteres"
    if(len(palabraIntroducida)<5):
        return "Tiene menos de 5 caracteres"
    if(palabraIntroducida.lower() == palabraGenerada):
        return "Acertaste"
    else:
        if(palabraIntroducida[0].lower() == palabraGenerada[0]):
            auxiliar += palabraIntroducida[0].lower()
        if(palabraIntroducida[1].lower() == palabraGenerada[1]):
            auxiliar += palabraIntroducida[1].lower()
        if(palabraIntroducida[2].lower() == palabraGenerada[2]):
            auxiliar += palabraIntroducida[2].lower()
        if(palabraIntroducida[3].lower == palabraGenerada[3]):
            auxiliar += palabraIntroducida[3].lower()
        if(palabraIntroducida[4].lower() == palabraGenerada[4]):
            auxiliar += palabraIntroducida[4].lower()
        return auxiliar


def game():
    acertado = True
    palabraAleatorio = palabraAleatoria()
    
    while(acertado):
        print("Introduce una palabra de 5 letras")
        palabra = raw_input()
        resultado = compararPalabras(palabra,palabraAleatorio)
        if(resultado == "Acertaste"):
            acertado = False
        print(resultado)

game()