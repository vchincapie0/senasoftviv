#Creación clase auto:
class Auto:
    #Creacion de objetos de la clase auto
    def __init__(self,marca,kilometros,año,color):
        self.__marca = marca 
        self.__kilometros = kilometros
        self.__año = año
        self.__color = color

    #Creacion de método definiendo si el auto esta encendido o apagado
    def arrancar(self,arrancamos):
        self.encendido = arrancamos
        if (self.encendido):
            return 'El auto esta encendido'
        else:
            return 'El auto esta apagado'
     
    def __str__(self):
        return 'El auto es un {}, tiene {} kilometros, es del año {}, y es de color {}'.format(self.__marca, self.__kilometros, self.__año, self.__color)
    

#Insercion de instancias para la clase auto:    
miCoche = Auto('Renault', 3500, 2015, 'Rojo')
miCoche2 = Auto('Chevrolet', 2000, 1997, 'Gris Oscuro')
miCoche3 = Auto('Volvo', 1500, 2019, 'Negro')

#Impresion de datos de la clase auto:
print(str(miCoche))
print(miCoche.arrancar(True))
print()
print(str(miCoche2))
print(miCoche2.arrancar(False))
print()
print(str(miCoche3))
print(miCoche3.arrancar(True))