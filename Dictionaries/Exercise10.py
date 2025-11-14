# Escribir un programa que permita gestionar la base de datos de clientes de una
# empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
# cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre,
# dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se
# trata de un cliente preferente. El programa debe preguntar al usuario por una opción
# del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4)
# Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la
# opción elegida el programa tendrá que hacer lo siguiente:
# 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a
# la base de datos.
# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3. Preguntar por el NIF del cliente y mostrar sus datos.
# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y
# nombre.
# 6. Terminar el programa.
import os

def limpiar():
    os.system("clear")
def continuar():
    tecla=input("Pulsa cualquier tecla para regresar al menú ")

def anadir_cliente():
    print("HA ELEGIDO AÑADIR UN CLIENTE")

    nif=input("Introduzca el NIF del cliente a añadir: ")

    if nif in clientes:
        print("Error, el cliente que intenta añadir ya existe")
        continuar()

    else:
        print(f"Se va a añadir al cliente con NIF {nif}...")
        print("Introduzca los datos relativos a este: ")
        nombre=input("Nombre: ")
        direccion=input("Dirección: ")
        telefono=input("Teléfono: ")
        correo=input("Correo electrónico: ")
        preferente=("¿Es preferente? (si|no) ")

        while preferente != "si" or preferente != "no":
            print("Respuesta a preferente no válida. Inténtelo de nuevo")
            preferente=("¿Es preferente? (si|no) ")

        if preferente == "si":
            preferente=True
        else:
            preferente=False
        
        clientes[nif]={
            "Nombre": nombre,
            "Dirección": direccion,
            "Teléfono": telefono,
            "Correo Electrónico": correo,
            "Preferente": preferente
        }
        print("El cliente se ha añadido con éxito")
        continuar()
    
def eliminar_cliente():
    print("HA ELEGIDO ELIMINAR UN CLIENTE")
    nif=input("Introduzca el NIF del cliente a eliminar: ")

    if nif in clientes:
        print(f"Cliente encontrado con NIF {nif}")
        resp=input("¿Está seguro de que desea eliminarlo? (si|no) ")

        while resp != "si" or resp != "no":
            print("Respuesta no válida, inténtelo de nuevo")
            resp=input("¿Está seguro de que desea eliminarlo? (si|no) ")

            if resp == "no":
                print("Se ha cancelado la acción de borrar al cliente")
                continuar()
            else:
                print("Se va a borrar al cliente...")
                del clientes[nif]
                print("El cliente ha sido eliminado")
                continuar()
    else:
        print(f"No se ha encontrado ningún cliente con NIF {nif}")
        continuar()

def mostrar_cliente():
    print("HA ELEGIDO MOSTRAR UN CLIENTE")
    nif=input("Introduzca el NIF del cliente a mostrar: ")

    if nif in clientes:

def listar_clientes():
    print("HA ELEGIDO MOSTRAR TODOS LOS CLIENTES")

def listar_preferentes():
    print("HA ELEGIDO MOSTRAR LOS CLIENTES PREFERENTES")

#-----Comienzo del programa-----
limpiar()

opc=1
clientes={}

while opc!=6:
    limpiar()
    print("GESTION DE BASE DE DATOS DE CLIENTES")
    print("------------------------------------")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar los clientes preferentes")
    print("6. Terminar")

    opc=int(input("Seleccione la opción por el número (1|2|3|4|5|6): "))

    if opc == 1:
        anadir_cliente()  
    elif opc == 2:
        eliminar_cliente()
    elif opc == 3:
        mostrar_cliente()
    elif opc == 4:
        listar_clientes()
    elif opc == 5:
        listar_preferentes()
    elif opc == 6:
        print("Saliendo de la gestión de la Base de Datos del cliente")
        print("Gracias por usar nuestro programa")
        print("¡Ten un bonito día!")
        continue
    else:
        print("Error, ha elegido una opción no válida")
        continuar()