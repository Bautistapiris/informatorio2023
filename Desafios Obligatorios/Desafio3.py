import random

# Pedir al jugador que ingrese su nombre
nombre = input("Por favor ingrese su nombre: ")

# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
print(f"{nombre}, el número a adivinar está entre 1 y 100. Solo tienes 8 intentos para adivinarlo. ¡Suerte!")

# Generar aleatoriamente un número entero entre 1 y 100
numero_a_adivinar = random.randint(1, 100)

# Definir la cantidad de intentos disponibles
intentos_disponibles = 8

# Iniciar el juego
while intentos_disponibles > 0:
    # Informarle al jugador cuántos intentos le quedan y solicitarle que ingrese un número
    print(f"Te quedan {intentos_disponibles} intentos.")
    numero_ingresado = input("Ingresa un número: ")
    
    # Verificar si el número ingresado es un entero válido
    if not numero_ingresado.isdigit():
        print("El número ingresado no es un número entero. Inténta de nuevo.")
    else:
        # Convertir el número ingresado a entero
        numero_ingresado = int(numero_ingresado)
        
        # Descontar un intento
        intentos_disponibles -= 1
        
        # Verificar si el número ingresado es menor al número a adivinar
        if numero_ingresado < numero_a_adivinar:
            print("El número a adivinar es mayor. Inténta de nuevo.")
        # Verificar si el número ingresado es mayor al número a adivinar
        elif numero_ingresado > numero_a_adivinar:
            print("El número a adivinar es menor. Inténta de nuevo.")
        # Si el número ingresado es igual al número a adivinar, el usuario ha ganado
        else:
            intento_actual = 8 - intentos_disponibles + 1
            print(f"¡{nombre}, has ganado en el intento número {intento_actual}!")
            break

# Si el usuario no adivina el número en los 8 intentos, se debe mostrar el número que tenía que adivinar
if intentos_disponibles == 0:
    print(f"Se agotaron los intentos. El número a adivinar era {numero_a_adivinar}. ¡Inténtalo de nuevo la próxima vez, {nombre}!") 