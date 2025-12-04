#Escribir una función que calcule el máximo común divisor de dos números y otra que
#calcule el mínimo común múltiplo

def maximoComunDivisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def minimoComunMultiplo(a, b):
    return abs(a * b) // maximoComunDivisor(a, b)

print(maximoComunDivisor(12, 18))
print(minimoComunMultiplo(12, 18))

print(maximoComunDivisor(8, 20))
print(minimoComunMultiplo(8, 20))
