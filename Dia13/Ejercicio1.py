#Cree al menos una base de datos que se llame Personas. Luego introduzca al menos 10 personas a esa base de datos. 
import sqlite3

conexion= sqlite3.connect('Personas.db')
cursor=conexion.cursor()

cursor.execute('CREATE TABLE PERSONAS(NOMBRE VARCHAR(20),APELLIDO VARCHAR(20),EDAD INTEGER,GENERO VARCHAR(20))')
personas = [
    ('Andres','Alzate',19,'Masculino'),
    ('Kevin','Albarracin',26,'Masculino'),
    ('Karol','Marroquin',21,'Femenino'),
    ('Juan Diego','Rubio',18,'Masculino'),
    ('Michael','Quintero',23,'Masculino'),
    ('Diego','Aguilar',18,'Masculino'),
    ('Vivian','Hincapie',25,'Femenino'),
    ('Martha','Escobar',34,'Femenino'),
    ('Jose','Montoñez',16,'Masculino'),
    ('Ramiro','Jimenez',32,'Masculino'),
    ('Rosario','Quezada',54,'Femenino'),
]

cursor.executemany('INSERT INTO PERSONAS VALUES(?,?,?,?)',personas)
conexion.commit()
conexion.close()