#Escribir un programa que almacene el diccionario con los créditos de las asignaturas
#de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
#muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
#tiene <créditos> créditos, donde <asignatura> es cada una de las
#asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
#también el número total de créditos del curso

import os
os.system("clear")

asignaturas={
    "Matemáticas": 6,
    "Lengua": 5,
    "Física": 6,
    "Química": 6,
    "Geografía": 5,
    "Historia": 5
}

suma=0
for asig,creditos in asignaturas.items():
    suma+=creditos
    print(f"{asig} tiene {creditos} créditos")
print(f"En total, todas las asignaturas suman {suma} créditos")