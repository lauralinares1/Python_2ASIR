#Escribir una función que reciba un número entero positivo y devuelva su factorial

def factorial(numero):
    fac=1
    for i in range(1,numero+1):
        fac=fac*i
    return fac

fact=factorial(4)
print(fact)