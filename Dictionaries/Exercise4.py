#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
#por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
#el nombre del mes.

import os
os.system("clear")

print("Fecha de nacimiento en formato dd/mm/aaaa \n")
nacimiento=input("Introduzca su fecha de nacimiento: ")

mes={
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}