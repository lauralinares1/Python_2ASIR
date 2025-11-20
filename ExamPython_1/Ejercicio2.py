print("BIENVENIDO AL PROGRAMA MATEMÁTICO")
print("---------------------------------")

resp='hola'

def mensaje(operando1,operador,operando2,total):
    print(f"El valor de {operando1} {operador} {operando2} = {total}")

while resp!='salir':
    print("Introduzca la operación a realizar en el siguiente formato: ")
    print("operando1 operador operando 2")
    print("Para salir del programa, escriba 'salir'")
    resp=input("Introduzca su consulta: ")

    if resp == 'salir':
        print("Saliendo del programa...")
        print("¡Que tenga un buen día!")
        continue

    operandos=resp.split(" ")

    if len(operandos) != 3:
        print("ERROR. No se han introducido tres valores")
        print("Volviendo al menú...")
        continue
    else:
        op1=int(operandos[0]) # el primer operador
        op2=int(operandos[2]) # el segundo operador
        if operandos[1] == '+':
            suma=op1+op2
            mensaje(op1,operandos[1],op2,suma)
        elif operandos[1] == '-':
            resta=op1-op2
            mensaje(op1,operandos[1],op2,resta)
        elif operandos[1] == '*':
            producto=op1*op2
            mensaje(op1,operandos[1],op2,producto)
        elif operandos[1] == '/':
            cociente=op1/op2
            mensaje(op1,operandos[1],op2,cociente)
        elif operandos[1] == '**':
            potencia=op1**op2
            mensaje(op1,operandos[1],op2,potencia)
        else:
            print("Error, el operador utilizado no se reconoce")