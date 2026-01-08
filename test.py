lista = []
opc = 1

while opc != 9:
    print("Elija una de las opciones posibles:")
    print("1. Añadir número a la lista de números")
    print("2. Añadir número de la lista en una posición")
    print("3. Decir longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un elemento diciendo el número")
    print("6. Contar números")
    print("7. Decir la posición de un número")
    print("8. Mostrar números")
    print("9. Salir")
    opc = int(input("Indique su opción: "))

    if opc == 1:
        num = int(input("Introduzca el número a añadir: "))
        lista.append(num)
        print("El número ha sido añadido correctamente a la lista")

    elif opc == 2:
        num = int(input("Introduzca el número a añadir: "))
        pos = int(input("Introduzca la posición en la que desea añadirlo: "))
        pos = pos - 1
        if pos >= 0 and pos <= len(lista):
            lista.insert(pos, num)
        else:
            print("Se ha indicado una posición incorrecta")

    elif opc == 3:
        longitud = len(lista)
        print(f"La longitud de la lista es: {longitud}")

    elif opc == 4:
        if len(lista) > 0:
            print("Se va a eliminar el último elemento")
            lista.pop()
            print("El último elemento se ha eliminado")
        else:
            print("La lista está vacía")

    elif opc == 5:
        num = int(input("Introduzca el número a eliminar: "))
        if num in lista:
            lista.remove(num)
            print(f"El número {num} ha sido eliminado")
        else:
            print("El número no está en la lista")

    elif opc == 6:
        suma = 0
        for n in lista:
            suma += n
        print(f"La suma de los números es {suma}")

    elif opc == 7:
        num = int(input("Introduzca el número que desea buscar: "))
        if num in lista:
            print(f"La posición del número en la lista es: {lista.index(num) + 1}")
        else:
            print(f"El número {num} no se encuentra en la lista")

    elif opc == 8:
        for n in lista:
            print(n, end=" ")
        print("")

    elif opc == 9:
        print("Saliendo...")
