print("PROGRAMA CÁLCULO DE IRPF EN FUNCIÓN DE SU RENTA")
print("-----------------------------------------------")
renta=float(input("¿Cuál es su renta? "))

auxiliar=renta

pago=0

if renta > 12450: # si la renta es mayor que el primer tramo
    if renta >= 0 and renta <= 12450: # mira si supera el tramo para saber si es el maximo o no
        pago+=renta*(19/100) # si no lo es, se calcula con su renta directamente
    else:
        pago+=12450*(19/100) # si es mayor, usa el valor maximo
# se repite el mismo cálculo en los demás tramos
if renta > 20200:
    if renta >= 1451 and renta <= 20200:
        variable=renta-12450
        pago+=variable*(24/100)
    else:
        pago+=7750*(24/100)

if renta > 35200:
    if renta >= 20201 and renta <= 35200:
        variable=renta-20200
        pago+=variable*(30/100)
    else:
        pago+=15000*(30/100)

if renta > 35200:
    variable=renta-35200
    pago+=variable*(37/100)


print(f"El pago que debe realizar en total es de {pago} €")