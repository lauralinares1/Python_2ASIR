# Escribir un programa que gestione las facturas pendientes de cobro de una
# empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
# factura será el número de factura y el valor el coste de la factura. El programa debe
# preguntar al usuario si quiere añadir una nueva factura, pagar una existente o
# terminar. Si desea añadir una nueva factura se preguntará por el número de factura
# y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará
# por el número de factura y se eliminará del diccionario. Después de cada operación
# el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la
# cantidad pendiente de cobro.

def limpiar():
    import os
    os.system("clear")

limpiar()

facturas={}
cantidadcobrada=0
cantidadpendiente=0

num=1

while num == 1 or num == 2:
    limpiar()
    print("----PROGRAMA DE GESTIÓN DE FACTURAS----\n")
    print("OPCIONES POSIBLES: \n")
    print("1. Añadir nueva factura (introducir '1')")
    print("2. Pagar una factura (introducir '2')\n")
    print("Para salir, introduzca cualquier otra cosa")
    num=int(input("Por favor, seleccione la opción que desea realizar: "))

    if num != 1 and num != 2:
        print("Ha seleccionado otra opción distinta")
        print("Saliendo del programa...")
        n=input("Pulse cualquier tecla para cerrar esta ventana ")
        continue

    if num == 1:
        print("Se va a añadir una nueva factura \n")
        numerofactura=int(input("Introduzca el número de factura: "))
        costefactura=float(input("Introduzca el coste de la factura nº %d: " %numerofactura))
        facturas[numerofactura]=costefactura
        cantidadpendiente+=costefactura
        n=input("Pulse cualquier tecla para continuar ")
    elif num ==2:
        print("Se va a pagar una factura \n")
        numerofactura=int(input("Introduzca el número de factura a pagar: "))
        del facturas[numerofactura]
        print("Se ha pagado la factura \n")
        cantidadpendiente=cantidadpendiente-(float(facturas.get(numerofactura)))
        cantidadcobrada+=facturas.get(numerofactura)
        n=input("Pulse cualquier tecla para continuar ")

    print(f"La cantidad pendiente a pagar es de {cantidadpendiente} €")
    print(f"Hasta ahora, se han pagado {cantidadcobrada} € en facturas")
    n=input("Pulse cualquier tecla para volver al menú ")