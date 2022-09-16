# Acá va a un comentario
if 3 > 5: # Acá va a un comentario
    print('Esto no se va a imprimir')

# if 5 > 3: # Acá va otro comentario
    # print('5 es mayor a 3')


x = 5
y = 'chanchito feliz'

print(x, y)

correo = 'chanchito@feliz.com'

print(correo)

_mi_var = 'chanchito'
MIVAR = 'chanchito'
a, b, c = 'Lala', 'Lele', 'Lili'

# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

# print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'mundo'

# print(inicio + final)

palabra = 'hola mundo' # string
oracion = "hola mundo comilla doble" # string

entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j

# print(palabra, oracion, entero, conDecimales, complejo)

lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista2 = lista.copy()  #copia la lista pero si se le agrega un nuevo elemento y llamas a las 2 listas la copiada no le llegara el ultimo agregado
lista.append('Chanchito triste')
# lista.clear()     #limpia la lista
# print(lista, lista2.count(3))  # count sirve para ver cuantas veces se repite un elemento en la lista
# print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

# print(lista[2])

# lista.pop() # este elimina el último elemento de la lista
# lista.remove('Hola') # este elimina un elemento por su valor

lista.reverse()  # invierte el orden de la lista 
lista.sort() # para ordenar la lista, pero tiene que tener el mismo tipo de dato
tupla = ('hola', 'mundo', 'somos', 'tupla')     # el metodo index sirve para saber la poscion de un elemento que digita el usuario
listaDeTupla = list(tupla) # pasar de tupla a una lista , solo hay q poner 'list' y pasarle la tupla
# print(listaDeTupla)

rango = range(6)  # salida es (0,6)
# print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre']) obtener valor de nombre
# print(diccionario['raza'])
# print(diccionario.get('nombre'))  lo mismo pero sin corchetes 
# diccionario['nombre'] = 'fluffy' esto es para cambiar el valor 
# print(len(diccionario))

diccionario['ronronea'] = 'Si'  #agregar otra propiedad al diccionario(como nombre,raza,edad)

# print(diccionario)
# diccionario.pop('ronronea')  eliminar valor
# diccionario.popitem() elimina ultimo valor agregado al dicc
# copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario) #elimina el contenido del diccionario
# del diccionario['ronronea']
diccionario.clear()
# print(diccionario, copiaGatito)

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)  #crear diccionario con dict
print(perritos)

verdadero = True
falso = False

print(verdadero, falso)
