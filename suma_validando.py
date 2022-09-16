'''
a diferencia del otro script de suma este valida en el momento de ingresar
cada numero, para verificar si es un entero o no, en cambio el otro espera 
al termino de su ejecucion
'''
num1 = input('Ingresa el primer valor: ')
try: #intenara pasar en caso de q el usuario digite un string y no un entero a un entero sino el programa se caera
    primero = int(num1)
except: # en caso de que no paso eso lo del entero, entonces se asiga el string error_uno
    primero = 'error_uno'

if primero == 'error_uno':
    print('Error, solo puedes ingresar numeros enteros')
    exit() #termina el programa hasta ahi

num2= input('Ingresa segundo valor: ')
try: 
    segundo = int(num2)
except:
    segundo = 'error_dos'

if segundo == 'error_dos':
    print('Error, solo puedes ingresar numeros enteros')
    exit()

print('La suma de los numeros es:',primero + segundo) 