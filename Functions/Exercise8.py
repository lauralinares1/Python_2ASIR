#Escribir una función que reciba una muestra de números en una lista y devuelva un
#diccionario con su media, varianza y desviación típica
import math

def mediaNumeros(numeros):
    suma=0
    for i in numeros:
        suma+=i
    media=suma/len(numeros)
    return media

def varianzaNumeros(numeros,media):
    diferencia=0
    promedio=0
    for i in numeros:
        diferencia=i-media
        diferencia=diferencia*diferencia
        promedio+=diferencia
    varianza=promedio/(len(numeros)-1)
    return varianza

def desviacionTipicaNumeros(varianza):
    desviacion=math.sqrt(varianza)
    return desviacion

def operacionesNumeros(numeros):
    dicc={}
    media=mediaNumeros(numeros)
    varianza=varianzaNumeros(numeros,media)
    desviaciontipica=desviacionTipicaNumeros(varianza)

    if varianza < media:
        varianza="baja"
    elif varianza == media:
        varianza="cero"
    else:
        varianza="alta"

    dicc["Media"]=media
    dicc["Varianza"]=varianza
    dicc["Desviación Típica"]=round(desviaciontipica,2)

    return dicc


listanumeros=[1, 2, 3, 4, 5, 10]

diccionario=operacionesNumeros(listanumeros)

print(diccionario)
