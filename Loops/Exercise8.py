#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

import os
os.system("clear")

num=int(input("Por favor, introduzca un número entero positivo: "))

if num < 0:
    print(f"El número {num} no es un entero positivo")
else:
    acumulador=1
    for n in range(1,num+1,2):
        for m in range(n,0,-2):
            print(m, end=" ")
        print("")