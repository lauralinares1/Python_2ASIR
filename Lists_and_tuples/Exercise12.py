#Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando
#cada vector fila en una lista.

import os
os.system("clear")

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [-1, 0],
    [0, 1],
    [1, 1]
]

C = []  # matriz resultado

for i in range(2):  # 2 filas en A
    fila = []
    for j in range(2):  # 2 columnas en B
        suma = 0
        for k in range(3):  # 3 columnas en A / 3 filas en B
            suma += A[i][k] * B[k][j]
        fila.append(suma)
    C.append(fila)

print("Producto de las matrices:")
for fila in C:
    print(fila)
