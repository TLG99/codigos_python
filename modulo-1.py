import modulos as xs  # el as es para cambiar el nombre al modulo
from camelcase import CamelCase  #el from es de donde viene el modulo y el import es la funcion en especifica de nuestro modulo, se puede importar mas de una funcion con la ','

print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()    #todas instrucciones se siguen de la pagina pypi.org, donde se encuentran las librerias, su instalacion y descripcion de como usasarlas
s = 'esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)

#pip list para ver mis librerias instaladas
# para desinstalar un modulo basta con: pip uninstall (nombre)