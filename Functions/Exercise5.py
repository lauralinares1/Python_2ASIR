#Escribir una función que calcule el área de un círculo y otra que calcule el volumen
#de un cilindro usando la primera función
import math


def areacirculo(radio):
    area=math.pi*(radio**2)
    return area

def volumencirculo(altura,radio):
    area=areacirculo(radio)
    volumen=area*altura
    return volumen

circulo=volumencirculo(6,2)

print(round(circulo,2))