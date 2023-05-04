#-Escribe un programa que solicite al usuario un número decimal y luego 
#imprima la parte entera y decimal por separado
numero = float(input("Ingresa un numero con decimal: "))
numero_entero = int(numero)
numero_decimal = round(numero - numero_entero, 2)
print(f"La parte entera del numero ingresado es: {numero_entero}")
print(f"La parte decimal del numero ingresado es: {numero_decimal}")
