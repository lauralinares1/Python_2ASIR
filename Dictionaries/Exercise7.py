# Escribir un programa que cree un diccionario simulando una cesta de la compra. El
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
# que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
# compra y el coste total, con el siguiente formato
# Lista de la compra
# Artículo 1 Precio
# Artículo 2 Precio
# Artículo 3 Precio
# … …
# Total Coste

import os
os.system("clear")

cesta={}

articulo=""
contador=1

while articulo != "salir":
    print("\nPara salir introduzca 'salir' \n")
    articulo=input("Introduzca el artículo nº %d: " %contador)
    if articulo == "salir":
        continue
    precio=float(input("Introduzca el precio del artículo '%s': " %articulo))
    cesta[articulo]=precio
    contador+=1

suma=0
print("\nLista de la compra \n")
print("----------------------")
for a,p in cesta.items():
    print(f"{a}          {p} €")
    suma+=p
print("-----------------------")
print(f"Total             {round(suma,2)} €")