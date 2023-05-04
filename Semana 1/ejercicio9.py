#Escribe un programa que solicite al usuario dos números y luego imprima la suma, la resta,
# la multiplicación y la división de los dos números.
numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese otro número: '))
resultado_suma = numero1 + numero2
resultado_resta = numero1 - numero2
resultado_multiplicacion = numero1 * numero2
resultado_division_int = numero1 // numero2
print(f'El resultado de la suma es:{resultado_suma}, el de la resta:{resultado_resta}, el de la multiplicacion:{resultado_multiplicacion} y el de la division:{resultado_division_int}')