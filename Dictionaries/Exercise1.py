#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.

import os
os.system("clear")

diccionario={'Euro':'€','Dollar':'$', 'Yen':'¥'}
divisa=input("Introduzca la divisa que desea consultar: ")

encontrado=False
for clave,valor in diccionario.items():
    if clave == divisa:
        encontrado=True
        print(f"La divisa de {divisa} es: {valor}")

if not encontrado:
    print("No se ha encontrado esa divisa")
