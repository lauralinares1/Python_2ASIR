capital=float(input("Por favor, introduzca el capital: "))
interes=float(input("¿Cuál es el tipo de interés? "))
anyos=int(input("¿Cuántos años pretende invertir? "))

print("VALOR FUTURO")
for i in range(1,anyos+1):
    valor_futuro=capital*((1+(interes/100))**i)
    print(f"El valor futuro del año nº {i} es de: {valor_futuro}")