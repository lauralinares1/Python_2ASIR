# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
# con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
# diccionario generado con la función anterior y devuelva una tupla con la palabra más
# repetida y su frecuencia.

def crearDiccionario(cadena):
    dict={}
    palabras=cadena.split(" ")
    for p in palabras:
        if p in dict:
            dict[p]+=1
        else:
            dict[p]=1
    return dict

def palabraMasRepetida(diccionario):
    palabra="a"
    repeticiones=0
    for p,r in diccionario.items():
        if repeticiones < int(r):
            palabra=p
            repeticiones=r
    return (palabra,repeticiones)

cadenausuario=input("Escribe la cadena de la que quiere contar las palabras: ")
diccionariousuario=crearDiccionario(cadenausuario)
palabrausuario=palabraMasRepetida(diccionariousuario)

print("La palabra más usada en la cadena es:")
print(f"La palabra '{palabrausuario[0]}' que se repite {palabrausuario[1]} veces")