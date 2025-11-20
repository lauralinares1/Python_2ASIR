monedas=[5,2,1] # tipo de moneda

cantidadeuros=int(input("¿Cuál es su cantidad entera de euros? "))

mon5=cantidadeuros//monedas[0] # se calculan cuantas monedas de 5 se necesita

variable=cantidadeuros-(mon5*monedas[0]) # se resta lo ya calculado al total y se almacena en una variable auxiliar

mon2=variable//monedas[1] # se calculan las monedas de 2

variable-=(mon2*monedas[1]) # se resta al total

mon1=variable//monedas[2] # se calculan las monedas de 1

print(f"Para la cantidad proporcionada de {cantidadeuros} se usan {mon5} monedas de {monedas[0]} €, {mon2} monedas de {monedas[1]} € y {mon1} monedas de {monedas[2]} €")