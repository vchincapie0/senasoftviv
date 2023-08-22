#Cree un fichero y ábralo en modo escritura, luego asigne un texto a una variable e insértelo en el fichero. Por último, visualice el documento.txt si fue escrito correctamente.

from io import open

#Se abre el fichero en modo escritura 'w'
fichero=open('ejercicioFichero.txt','w')
texto='Dia 11\nEste es el ejemplo del ejercicio 1'
fichero.write(texto)
fichero.close()