#Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159
r = float(input('Ingrese el radio del circulo: '))
area = 3.14159 * r ** 2 
circunferencia = 2 * 3.14159 * r
diametro = r * 2
print(f'El diametro del circulo es: {diametro}, la circunferencia: {circunferencia} y el area: {area}')
