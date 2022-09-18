
from optparse import Values
import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'Nupangui19',
    database = 'curso'
)

cursor = midb.cursor()

#listar datos
# cursor.execute('select * from USUARIO')
# resultado = cursor.fetchall() #devuelve todos los datos de la db
# print(resultado)

#a diferencia con el de arriba este con el limit nos muestra solo el 1er resultado de la db
cursor.execute('select * from USUARIO limit 1')
resultado = cursor.fetchall() #devuelve todos los datos de la db
print(resultado)

#para insertar datos
#sql = 'insert into USUARIO (EMAIL, USERNAME, EDAD) VALUES(%s, %s, %s)'
#values = ('tomas.correo@gmail.com', 'tomaxx', 22)
#cursor.execute('show create table USUARIO') #te muestra la db
#cursor.execute(sql,values)
#resultado = cursor.fetchone() #devuelve el primer valor de la db
#midb.commit()  #commit toma los datos y ejecuta la consulta directamernte en la base de datos

#print(cursor.rowcount)

#actualizar datos
# sql = 'update USUARIO set email = %s where ID = %s'
# values = ('tomasg.correo@gmail.com', 4)
# cursor.execute(sql,values)
# midb.commit()

#eliminar datos
# sql = 'delete from USUARIO where ID = %s'
# values =(4, ) #es necesario la ',' y el espacio
# cursor.execute(sql,values)
# midb.commit()


