#Escribir una función que reciba una muestra de números en una lista y devuelva otra
#lista con sus cuadrados

def cuadradoNumeros(numeros):
    lista=[]
    for i in numeros:
        lista.append(i*i)
    return lista

listanumeros=[1,2,3,4,5,6,7,8,9,10]
cuadrados=cuadradoNumeros(listanumeros)
print(cuadrados)