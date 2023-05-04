texto = input('Ingrese cualquier texto: ').lower()
letras = []
letras.append(input("Ingrese la primer letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercer letra: ").lower())
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
print(f'La palabra Python {dic[buscar_palabra_python]} se encuentra mencionada en el texto')
