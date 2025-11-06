#Escribir un programa que cree un diccionario vacío y lo vaya llenado con
#información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
#electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
#debe imprimirse el contenido del diccionario.

import os
os.system("clear")

usuario={
    "nombre":"",
    "edad":"",
    "sexo":"",
    "telefono":"",
    "email":""
}

for clave in usuario.keys():
    var=input("\nIntroduzca su %s: " %clave)
    usuario[clave]=var
    print("\n-----Los datos introducidos hasta ahora son: -----\n")
    for clave,valor in usuario.items():
        print(f"{clave} --> {valor}")

print("El usuario ha sido registrado correctamente \n")
print("Mostrando información... \n")
for clave,valor in usuario.items():
    print(f"{clave} --> {valor}")
