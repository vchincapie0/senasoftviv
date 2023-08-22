#Serialice un diccionario utilizando el método dump. El archivo una vez serializado debe mostrarnos un mensaje que nos diga que no se puede abrir.

import pickle
#Creacion de diccionario
diccionario={'Vivian':26,'Maria':27,'Daniel':26,'Pedro':34}

#Creacion y apertura de fichero en binario 
fichero=open('diccionario','wb')
pickle.dump(diccionario,fichero) #codificación del diccionario que esta dentro del fichero 
fichero.close()
