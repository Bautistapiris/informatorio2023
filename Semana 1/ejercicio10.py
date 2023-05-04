#Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros.
#Supón que el tipo de cambio es de 0.84 euros por dólar.
dolares = float(input('Ingrese la cantidad de dolares a convertir: '))
precio_cambio= 0.84
precio_Euro = dolares * precio_cambio
print(f'El resultado del cambio de {dolares} dolares es de {precio_Euro} euros en total')