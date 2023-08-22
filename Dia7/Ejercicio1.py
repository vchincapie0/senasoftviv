#Se crea la clase persona 
class Persona:
    #Creacion de atributos de la clase personas
    def __init__(self,nombre,edad,sexo,nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__nacionailidad = nacionalidad
    
    #Creacion de metodos de datos de Personales para la clase Persona
    def datosPersona(self):
        print(f'El nombre de la persona es: {self.__nombre}')
        print(f'La edad de la persona es: {self.__edad}')
        print(f'El sexo de la persona es: {self.__sexo}')
        print(f'La nacionalidad de la persona es: {self.__nacionailidad}')


#Insercion de instancias 
persona1 = Persona('Camila', 34, 'Femenino', 'Argentina')
persona2 = Persona('Ruben', 57, 'Masculino', 'Colombiano')
persona3 = Persona('Martha', 45, 'Femenino', 'Uruguaya')
persona4 = Persona('Ivan', 29, 'Masculino', 'Italiano')

#Imprimir los datos de cada persona registrada
persona1.datosPersona()
print()
persona2.datosPersona()
print()
persona3.datosPersona()
print()
persona4.datosPersona()

#Verificacion de encapsulamiento de variable "nombre"
persona1.nombre = 'Maria'