'''
a = open('ejemplo.txt')  #los permisos son 'a' para agregar algo al final del archivo, 'r' para leer, 'w' para modificar el archivo, 'x' para crear un archivo 
#print(a.read())  #read solo para leerlo completo, readline para leer de uno en uno
for x in a:
    print(x) #esto es para leer cada una de las lineas por separado(con saltos)

a.close()
'''
a = open('ejemplo.txt', 'a')

a.write('\nNueva linea de agregacion')

a.close()

