#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>.

import os
os.system("clear")

nombre=input("Introduzca su nombre: ")
edad=int(input("Introduzca su edad: "))
direccion=input("Introduzca su dirección: ")
telefono=int(input("Introduzca su telefono: "))

usuario={
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

print(f"{usuario.get("nombre")} tiene {usuario.get("edad")} años, vive en {usuario.get("direccion")} y su número de teléfono es {usuario.get("telefono")}")
usuario["nombre"]