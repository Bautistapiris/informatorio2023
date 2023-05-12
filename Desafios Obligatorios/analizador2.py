texto = input("Ingrese el texto para analizar: ")
print("A continuación, ingrese 3 letras para su análisis")
letras = []
letras.append(input("Ingrese letra 1: ".lower()))
letras.append(input("Ingrese letra 2: ".lower()))
letras.append(input("Ingrese letra 3: ".lower()))
print("\n")

#SEGUNDA PARTE
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print("CANTIDAD DE LETRAS")
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")
print("\n")

#TERCERA PARTE
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
print("\n")

#CUARTA PARTE
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")
print("\n")

#QUINTA PARTE
print("TEXTO INVERTIDO")
invertido = ""
for i in texto:
    invertido = i + invertido

print(f'el texto invertido seria:{invertido}')
print("\n")

#SEXTA PARTE
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")