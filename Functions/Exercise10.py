#Escribir una función que convierta un número decimal en binario y otra que convierta
#un número binario en decimal

def decimal_a_binario(num):
    if num == 0:
        return "0"
    binario = ""
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num //= 2
    return binario

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal

print(decimal_a_binario(10))
print(decimal_a_binario(25))

print(binario_a_decimal("1010"))
print(binario_a_decimal("11001"))
