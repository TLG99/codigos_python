#programa que multiplica sin el simbolo de mult
'''
a= 5
b = 7
resultado = 0

for x in range(a):
    resultado +=b

print(resultado)    
'''
'''
#invierte los strings
nombre = 'Tomas'
apellido = 'Gonzalez'

conc = nombre + ' ' + apellido

print(conc[::-1])  #para dar vueltas strings
'''
'''
# encontrar el menor numero de una lista
lista = [5,8,1,7,51,45,2,9,23,-1]
menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('el menor valor es', menor)
'''
'''
#funcion q devuelva el volumen de una esfera por su radio (4/3 * pi *3)
def volumen(numero):
    esfera = (4/3* 3.14 * numero**3)  # ** elevando numero
    return esfera

resultado= volumen(6)
print(resultado)
'''
'''
#funcion para ver si alguien es mayor de edad
def mayor_edad(edad):
    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')

pregunta = input('Indica tu edad:')
edad = int(pregunta)
mayor_edad(edad)
'''
'''
#Ver si un numero es par o impar con una funcion
def par(valor):
    if valor % 2 == 0:
        print('El numero es par')
    else:
        print('El numero es impar')    
    return valor

num = input('Coloque valor:')
entero = int(num)
par(entero)
'''
'''
#funcion q nos diga cuantas vocales tiene una palabra
palabra = input('Coloque una palabra:')
pal = 0
for x in palabra:
    y = x.lower()
    pal += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
print('La palabra contiene',pal,'vocales')        
'''
# escribir una aplicacion que reciba una cantidad ifninita de numeros hasta
# decir 'basta', luego que devuelva la suma de los numeros ingresados
'''
lista= []
print('Ingrese valores y para salir escriba "basta"')
while True:
    valor = input('Ingrese valores: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato Inválido')
            exit()
resultado = 0
for x in lista:
    resultado += x      

print('La suma de los numeros es de',resultado)          
'''
# escribir una funcion que reciba nombre y apellido y los agregue a un archivo

def nom_ap(nombre, apellido, edad):
    archivo = open('Nombre_completo.txt', 'a')
    archivo.write(nombre + ' ' + apellido + ' ' + edad + '\n')
    archivo.close()
    
pregunta1 = input('Coloque Nombre: ')
pregunta2 = input('Coloque Apellido: ')
pregunta3 = input('Coloque su Edad: ')
nom_ap(pregunta1, pregunta2, pregunta3)