#Escribe un programa que solicite al usuario una temperatura en grados 
#Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32
temp_c = float(input("Ingrese la temperatura en grados Celsius: "))
calc_fah = (temp_c * 1.8) + 32
print(f"El valor ingresado en Celsius {temp_c} es equivalente en grados Fahrenheit: {calc_fah}")