#Cree una base de datos personas con los siguientes requerimientos: nombre, edad,sexo,DNI. El DNI debe ser una clave primaria, por lo cual no se puede repetir. 

#En la base de datos que acaba de crear realice un CRUD(Crear,Leer,Actualizar,Eliminar)

import sqlite3

conexion= sqlite3.connect('Personas.db')
cursor=conexion.cursor()

#Creacion de tabla personas
cursor.execute('CREATE TABLE PERSONAS(DNI INTEGER PRIMARY KEY,NOMBRE VARCHAR(20),EDAD INTEGER,GENERO VARCHAR(20))') 


personas = [
    (1234567,'Andres Alzate',19,'Masculino'),
    (7890123,'Kevin Albarracin',26,'Masculino'),
    (4567890,'Karol Marroquin',21,'Femenino'),
    (9876543,'Juan Diego Rubio',18,'Masculino'),
    (2109876,'Michael Quintero',23,'Masculino'),
    (5432109,'Diego Aguilar',18,'Masculino'),
    (8765432,'Vivian Hincapie',25,'Femenino'),
    (1098765,'Martha Escobar',34,'Femenino'),
    (6789012,'Jose Montoñez',16,'Masculino'),
    (3456789,'Ramiro Jimenez',32,'Masculino'),
    (7294739,'Rosario Quezada',54,'Femenino'),
]

#Insercion de datos en tabla personas
cursor.executemany('INSERT INTO PERSONAS VALUES(?,?,?,?)',personas)

#Leer datos de la tabla personas:
cursor.execute('SELECT * FROM PERSONAS WHERE EDAD>25 AND GENERO="Femenino"')
leer = cursor.fetchall()
print(leer)

#Actualización de datos:
cursor.execute('UPDATE PERSONAS SET EDAD=26 WHERE DNI LIKE "%9%"')

#Eliminar datos: 
cursor.execute('DELETE FROM PERSONAS WHERE DNI=6789012')
conexion.commit()
conexion.close()