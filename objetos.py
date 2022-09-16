'''
la clase es la idea global del objeto
Un objeto contiene propiedades(sus caracteristicas) y metodos(las funciones lo que hace el objeto en si)
'''
'''
class Usuario: #las clases siempre empiezan con mayusculas
    def __init__(self, nombre, apellido):   #self hace referencias a las instacias, el init se usa siempre para las instancias
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):   
        print('Hola!, mi nombre es', self.nombre, self.apellido)


class Admin(Usuario): #esto es herencia ya que recibe de Usuario
    def superSaludo(self):
        print('Hola!, me llamo,', self.nombre, ' y soy administrador')

usuario = Usuario('Felipe', 'Feliz')

usuario.saludo()
usuario.nombre = 'Chanchito' #esto es para cambiar el nombre de la propiedad
usuario.saludo()
# # del usuario.nombre #eliminar propiedad
# # del usuario
# # print(usuario)

# admin = Admin('Super', 'Feliz')  #al ser herencia del Usuario este ya contiene el init(entonces no se coloca en Admin), por lo que a Admin hay que pasarle 2 parametros que son el de nombre y apellido
# admin.saludo() # tambien se puede acceder a los metodos de Usuario, desde admin                    
# admin.superSaludo() #metodo q se realizó en Admin
# usuario.superSaludo()  #pero no se puede llamar a los metodos y propiedades de la clase padre(La que hereda las cosas)
'''
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):   #al poner un init no se llamará el de la clase padre para corrgir eso se hace lo sgte
        Animal.__init__(self, nombre, onomatopeya)      #llamar a la clase padre con .__init__ y pasarle los argumentos(incluido el self)
        print('Hola, soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)   #super hace referencia a la clase padre, pero no hay que pasarle el self    
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()

