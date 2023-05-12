texto = input('Ingrese un texto: ').lower()
texto2 = input('Ingrese 3 letras a su eleccion: ').lower()
letras = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

for i in letras:
    veces = 0
    for y in texto:
        if i == y:
            veces += 1
    print('La letra', i, 'aparece', veces, 'veces')
    