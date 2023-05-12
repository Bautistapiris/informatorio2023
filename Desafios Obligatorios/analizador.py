#Desafío 2: Analizador de textos
#Requisitos técnicos:
#Se te pide crear un programa que le pida al usuario que ingresar un texto cualquiera, por ejemplo, un artículo o una frase.
#Luego el programa le va a pedir al usuario que también ingrese 3 letras a su elección.
#Nuestro código va a procesar esa información para realizar los análisis necesarios para devolverle al usuario la siguiente información:
#1- Cantidad de veces que aparece cada una de letras que eligió.
#2- Cuantas palabras hay en total en todo el texto.
#3- Cual es la primera letra y cuál es la última. (Indexación)
#4- Mostrar el texto en orden inverso.
#5- Decir si la palabra "python" aparece en el texto.

texto = input('Ingrese un texto: ')
print('Ingrese 3 letras a su eleccion: ')
letras = []
letras.append(input('Ingrese la primer letra: '.lower()))
letras.append(input('Ingrese la segunda letra: '.lower()))
letras.append(input('Ingrese la tercera letra: '.lower()))


cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f'La letra {letras[0]} se repite {cantidad_letras1} veces')
print(f'La letra {letras[1]} se repite {cantidad_letras2} veces')
print(f'La letra {letras[2]} se repite {cantidad_letras3} veces')

palabras = texto.split()
print(f'En el texto se encuentran un total de {len(palabras)} palabras ')

letra_inicial = texto[0]
letra_final = texto[-1]
print(f'La letra inicial es {letra_inicial} y la letra final es {letra_final}')

invertido = ""
for i in texto:
    invertido = i + invertido
print(f'el texto invertido seria:{invertido}')

buscar_palabra_python = 'python' in texto
dic = {True:'sí', False:'no'}
print(f'La palabra Python {dic[buscar_palabra_python]} si se encuentra mencionada en el texto')