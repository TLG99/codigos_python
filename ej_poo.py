
class Animal:
    def __init__(self, nombre, sonido, patas):
        self.nombre = nombre
        self.sonido = sonido
        self.patas = patas
    def presentacion(self):
        print("Hola soy un", self.tipo, "y mi sonido es el", self.sonido,"y tengo",self.patas,"patas")

class Perro(Animal):
    tipo = "perro"
    patas = ""

class Gato(Animal):
    tipo = "gato"
    patas = ""

class Mono(Animal):
    tipo = "mono"
    patas = ""

perro = Perro("Kaiser", "Ladrido", 5)
perro.presentacion()

gato = Gato("Luna", "Maullido", 6)
gato.presentacion()

mono = Mono("Pedro", "Grito", 3)
mono.presentacion()
