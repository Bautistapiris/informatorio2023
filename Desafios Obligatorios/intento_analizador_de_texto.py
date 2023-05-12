
def contador_numeros_letras (cadena):
    numeros = 0
    letras = 0

    for c in cadena:
        if c.isdigit():
            numeros += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
    return numeros, letras

texto = input('Ingrese un texto: ')
resultado = contador_numeros_letras(texto)
print('Cantidad de numeros: %i' %resultado[0])
print('Cantidad de letras: %i' %resultado[1])