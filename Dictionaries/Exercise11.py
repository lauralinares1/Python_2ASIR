# El directorio de los clientes de una empresa está organizado en una cadena de texto
# como la de más abajo, donde cada línea contiene la información del nombre, email,
# teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter
# de cambio de línea \n y la primera línea contiene los nombres de los campos con la
# información contenida en el directorio.
# "nif;nombre;email;teléfono;descuento\n01234567L;Luis
# González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macar
# ena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José
# Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen
# Sánchez;carmen@mail.com;667677855;15.7"
# Escribir un programa que genere un diccionario con la información del directorio,
# donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor
# otro diccionario con el resto de la información del cliente. Los diccionarios con la
# información de cada cliente tendrán como claves los nombres de los campos y
# como valores la información de cada cliente correspondientes a los campos. Es
# decir, un diccionario como el siguiente
# {'01234567L': {'nombre': 'Luis González', 'email':
# 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento':
# 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email':
# 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0},
# '63823376M': {'nombre': 'Juan José Martínez', 'email':
# 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2},
# '98376547F': {'nombre': 'Carmen Sánchez', 'email':
# 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}

import os
os.system("clear")

# Datos de ejemplo
directorio = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

# Dividir el directorio en líneas
lineas = directorio.strip().split('\n')

# Obtener los nombres de los campos desde la primera línea
campos = lineas[0].split(';')

# Crear el diccionario principal
directorio_clientela= {}

# Procesar cada línea de datos (empezando desde la segunda línea)
for i in range(1, len(lineas)):
    # Dividir los datos de cada cliente
    datos_cliente = lineas[i].split(';')
    
    # Crear el diccionario interno para este cliente
    cliente_dict = {}
    
    # Asignar cada valor a su campo correspondiente
    for j in range(len(campos)):
        if campos[j] == 'nif':
            # El NIF será la clave principal, no lo incluimos en el diccionario interno
            nif = datos_cliente[j]
        else:
            cliente_dict[campos[j]] = datos_cliente[j]
    
    # Agregar el cliente al directorio principal
    directorio_clientela[nif] = cliente_dict

# Mostrar el resultado
print("Directorio de clientes:")
for nif, datos in directorio_clientela.items():
    print(f"{nif}: {datos}")      