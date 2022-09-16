
def miFuncion():
    print('Mi primera función!')

# miFuncion()

def imprimeDato(*nombre): # para recibir mas argumentos
    print('El nombre completo es:', nombre[1])

# imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')   #en este caso se estan pasando 4 parametros cuando hay un solo argumento, solo cn el * es valido
                                                        # se imprimira la funcion pero en formato tupla
def nombreCompleto(apellido, nombre): #no importa el orden ya que esta definido 
    print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='Feliz')   aca estan asignados

def nombreCompleto2(**kwargs): #agrupamiento por diccionario
    print(kwargs['nombre'], kwargs['apellido'])


# nombreCompleto2(nombre='Chanchito', apellido='Feliz')


def miFuncion2(argumento = 'Chanchito'):  #en caso de no pasar un parametro, este quedara con 'Chanchito' pq esta asignado el argumento
    print(argumento)

# miFuncion2('Batman') #imprimira batman pq asi esta programado
# miFuncion2()       #pero si no pasamos el parametro queda el defecto del de arriba 

def miFuncionLista(lista):      #argumento como lista
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz'])  #pasar los parametros en modo lista


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i            #cuando se retorna un valor hay que asigar una variable

# nombres = concatenaNombres(['Chanchito', 'Feliz'])  #la q se encuentra aca
# print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)


