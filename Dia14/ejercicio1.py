#Cree una función de generar numeros pares de manera tradicional

limite=int(input('Ingrese la cantidad de pares que desea:'))
def pares(limite):
    num=1
    lista=[]
    while (num<limite):
        lista.append(num*2)
        num+=1
    return lista

print(pares(limite))

#Cree una funcion genera pares utilizando generadores
limite2=int(input('Ingrese la cantidad de pares que desea:'))
def pares2(limite2):
    num=1
    while(num<limite2):
        yield num*2

imprimir=pares2(limite2)
print(next(imprimir))