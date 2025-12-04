#Escribir una función que reciba una muestra de números en una lista y devuelva su
#media

def mediaNumeros(numeros):
    suma=0
    for i in numeros:
        suma+=i
    media=suma/len(numeros)
    return media

listanumeros=[1,2,3,4,5,6,7,8,9,10]
m=mediaNumeros(listanumeros)
print(m)