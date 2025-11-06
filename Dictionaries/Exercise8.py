# Escribir un programa que cree un diccionario de traducción español-inglés. El
# usuario introducirá las palabras en español e inglés separadas por dos puntos, y
# cada par <palabra>:<traducción> separados por comas. El programa debe
# crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
# en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
# no está en el diccionario debe dejarla sin traducir.

import os
os.system("clear")

diccionario={}

print("----PROGRAMA RECOPILADOR DE PALABRAS TRADUCIDAS----\n")
print("Formato a introducir : \n")
print("palabra:traduccion,palabra2:traduccion2,palabra3:traduccion3,palabraN:traduccionN \n")

cadena=input("Introduzca todas las palabras traducidas siguiendo el formato indicado: ")

traducciones=cadena.split(",")

for i in range(len(traducciones)):
    traduccion=traducciones[i].split(":")
    esp=traduccion[0]
    eng=traduccion[1]
    diccionario[esp]=eng

for p,t in diccionario.items():
    print(f"{p} --> {t}")

frase=input("Introduzca la frase que desee traducir: ")

palabras=frase.split(" ")

for i in range(len(palabras)):
    for pal,trad in diccionario.items():
        if palabras[i] == pal:
            print(trad,end=" ")