#Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad
#en años.
#Utiliza la función .split()
fecha = (input("Ingrese su fecha de naciomiento en el siguiente formato dd/mm/aaaa \n"))
dia, mes, anio = fecha.split("/")
if int(mes)>4: 
    edad = 2023 - int(anio) - 1
else:
    edad = 2023 - int(anio)
print("Su edad es: ", edad )