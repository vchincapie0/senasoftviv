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
    #Creacion de metodos de clase empleados
    def datosempleado(self,salario,puesto,vacaciones):
        print(f"Su salario es: {salario}")
        print(f'Su puesto de trabajo es: {puesto}')
        print(f'Sus dias de vacaciones son {vacaciones}')

#Creacion de instancias de clase empleados datospersonales y datosempleados
empleado1=Empleados('Camilo', 'Arias', 25, 'Masculino')
empleado1.datosPersonales()
empleado1.datosempleado(1200000, 'Técnico en soporte', 15)
print()
empleado2=Empleados('Julian', 'Fonseca', 36, 'Masculino')
empleado2.datosPersonales()
empleado2.datosempleado(2500000, 'Community Manager', 3)
print()
empleado3=Empleados('Karol', 'Gomez', 45, 'Femenino')
empleado3.datosPersonales()
empleado3.datosempleado(1560000, 'Agente de Servicio al Cliente', 5)







        