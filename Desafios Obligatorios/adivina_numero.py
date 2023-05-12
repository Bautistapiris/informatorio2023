import random 
nombre = input('Por favor ingrese su nombre: ').capitalize()
print(f'\nBienvenido {nombre}, debes adivinar el numero oculto.\nEl mismo se encuentra entre el 1 y el 100.\nTienes 8 intentos.\n¿Podras lograrlo?\n')
frases_intentos = ['¡Estas Cerca!', 'Sigue intentando', '¡Tal vez en la siguiente!','¡Vamos tu puedes!', 'No te desanimes flaco', 'No te rindas.', 'Casi', 'Es lo mejor de ti?','Corre forest! correee']

numero_ganador = random.randint(1, 100)  
intentos_disponibles = 8  
cumple_condicion = True 

while cumple_condicion:
   
    numero_ingresado = input(f'Ingrese un numero entre 1 y 100. Tus intentos disponibles son {intentos_disponibles}.\n Ingrese un numero elegido:  ')
    
    
    numero_ingresado_entero = int()
    if numero_ingresado.isdigit():
        numero_ingresado_entero = int(numero_ingresado)
    if not numero_ingresado.isdigit():
        print(f'\n¡RECUERDA!\nDebes ingresar un numero entero, entre 1 y 100.\n\'{numero_ingresado}\' no cumple las condiciones, vamos de nuevo..')
        continue
    
    eleccion_frase = random.choice(frases_intentos)
    
    if numero_ingresado_entero < numero_ganador and numero_ingresado_entero > 0:
        print(f'\n{eleccion_frase}\nEl numero ganador es mayor a \'{numero_ingresado}\'')
        intentos_disponibles -= 1
    if numero_ingresado_entero > numero_ganador and numero_ingresado_entero <= 100:
        print(f'\n{eleccion_frase}\nEl numero ganador es menor a \'{numero_ingresado}\'.')
        intentos_disponibles -= 1
    
    if numero_ingresado_entero <= 0 or numero_ingresado_entero > 100:
        print(f'\nEl numero ingresado debe estar entre 1 y 100.\n\'{numero_ingresado}\' no cumple las condiciones, vamos de nuevo..')
        continue
    
    if numero_ingresado_entero == numero_ganador:
        cumple_condicion = False
        ganador = f'\n¡BIEN!\nLo has adivinado en el intento {8 - intentos_disponibles} {nombre}! y te han sobrado {intentos_disponibles} intentos. \n¡Gracias por jugar!'
        if intentos_disponibles == 1:
            singular = ganador.replace('intentos', 'intento').replace('han', 'ha')
            print(singular)
        else:
            print(ganador)
    if intentos_disponibles == 0:
        cumple_condicion = False
        print(f'\n No lo lograste  {nombre.upper()}.\nSe te han acabado los intentos.\n El numero oculto era: \'{numero_ganador}\'.¡Gracias por jugar!\n')