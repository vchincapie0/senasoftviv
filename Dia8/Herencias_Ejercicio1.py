#Creación clase personas
class Persona:
    #Creacion atributos de la clase personas
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo 

    #Creacion metodo de clase personas que imprimira los atributos de la clase
    def datosPersonales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'El apellido de la persona es: {self.apellido}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')

#Creacion clase empleados
class Empleados(Persona):
    def datosempleado(self):
        print("Los datos de los empleados")



#Creacion de instancias de clase empleados datospersonales
empleado1 = Empleados('Camilo', 'Arias', 25, 'Masculino')
empleado1.datosPersonales()

print()
empleado2=Empleados('Julian', 'Fonseca', 36, 'Masculino')
empleado2.datosPersonales()

print()
empleado3=Empleados('Karol', 'Gomez', 45, 'Femenino')
empleado3.datosPersonales()







        