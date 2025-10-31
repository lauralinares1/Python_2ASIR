#Escribir un programa que guarde en un diccionario los precios de las frutas de la
#tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
#precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
#mostrar un mensaje informando de ello

import os
os.system("clear")

fruteria={
    "platano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

fruta=input("Introduzca la fruta que desea comprar: ").lower()
kilos=int(input("Introduzca los kilos que desea comprar: "))

if fruta in fruteria:
    print(f"El kilo de {fruta} está a {fruteria.get(fruta)} € \n")
    total=kilos*fruteria.get(fruta)
    print(f"El total de su compra sería de {total} €")
else:
    print("Error. La fruta no está disponible")