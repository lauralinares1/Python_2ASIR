num=int(input("Introduzca la altura que desea: "))

if num < 0:
    print("Número negativo no admitido")
else:
    for i in range((num-1),-1,-1):
        print((" " * i) + "*")