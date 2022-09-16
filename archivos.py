'''
c = open('ejemplo.txt', 'w') #agregara la linea pero borrara todo el contenido del archivo

c.write('\nagregaremos una nueva línea a nuestro archivo')

c.close()

x = open('ejemplo.txt')

print(x.read()) #lee el archivo con la nueva linea agregada
'''

import os  # os para eliminar carpetas o archivos de nuestro sistema

if os.path.exists('ejemplo.txt'):  #verifica si existe ese archivo
    os.remove('ejemplo.txt') # en tal caso elimina el archivo
else:
    print('El archivo no existe') #sino salta el sgte mensaje

os.rmdir('hola') # para eliminar una carpeta
