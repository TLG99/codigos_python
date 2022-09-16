num1 = input('Ingresa el primer valor: ')

try: #intenara pasar en caso de q el usuario digite un string y no un entero a un entero sino el programa se caera
    primero = int(num1)
except: # en caso de que no paso eso lo del entero, entonces se asiga el string chacnhito feliz
    primero = 'error'

num2= input('Ingresa segundo valor: ')
try: 
    segundo = int(num2)
except:
    segundo = 'error'

if primero == 'error' or segundo == 'error':
    print('El programa no se puede ejecutar, coloca solo numeros')
else:
    print('La suma de los numeros es:',primero + segundo)    