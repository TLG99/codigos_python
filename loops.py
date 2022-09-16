# i = 0

# while i < 5:
    # i += 1
    # if i == 3:
        # continue   #se salta la condicion dada 
    # print(i)

# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# for usuario in usuarios: #se pone el singular de la palabra para así poder llamarlo
    # print(usuario) #se imprime siempre el primero en este caso usuario

# usuario = 'Chanchito Feliz'

# for c in usuario:  # el c es por caracter, este imprimirá los caracteres, es decir, por separado no la palabra completa
    # print(c)


# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# for usuario in usuarios:
    # if usuario == 'roberto':
        # break
    # print(usuario)


# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# for usuario in usuarios:
    # if usuario == 'roberto':
        # continue  #continue hace q se salte el ciclo, break termina el progrmama hasta ahi
    # print(usuario)

# for x in range(3, 30, 5):  # el primer valor es de donde empieza, segundo hasta donde, tercero desde cuanto es el intervalo
    # print(x)
# else:
    # print('Hemos terminado!!')

usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas', 'Tomas']

edades = [24, 25, 26, 35, 54]

for usuario in usuarios:      #los for que se encuentren mas a la derecha son 
                                #los que se van ejutar primero antes de pasar al sgte for que se encuentra mas arriba
    for edad in edades:
        print(usuario, edad)

